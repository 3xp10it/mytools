#############################################################
###                                                  
###   ▄▄▄▄                ▄▄▄     ▄▄▄▄    ▀      ▄   
###  ▀   ▀█ ▄   ▄  ▄▄▄▄     █    ▄▀  ▀▄ ▄▄▄    ▄▄█▄▄ 
###    ▄▄▄▀  █▄█   █▀ ▀█    █    █  ▄ █   █      █   
###      ▀█  ▄█▄   █   █    █    █    █   █      █   
###  ▀▄▄▄█▀ ▄▀ ▀▄  ██▄█▀  ▄▄█▄▄   █▄▄█  ▄▄█▄▄    ▀▄▄ 
###                █                                 
###                ▀                                 
###                                                          
### name: xcdn.py
### function: try to get the actual ip behind cdn
### date: 2016-11-05
### author: quanyechavshuo
### blog: https://3xp10it.cc
#############################################################
import time
from exp10it import figlet2file
figlet2file("3xp10it",0,True)
time.sleep(1)

from exp10it import CLIOutput
from exp10it import get_root_domain
from exp10it import get_string_from_command
from exp10it import get_http_or_https
from exp10it import post_request
from exp10it import get_request


def domain_has_cdn(domain):
    # 检测domain是否有cdn
    # 有cdn时,返回一个字典,如果cdn是cloudflare，返回{'has_cdn':1,'is_cloud_flare':1}
    # 否则返回{'has_cdn':1,'is_cloud_flare':0}或{'has_cdn':0,'is_cloud_flare':0}
    CLIOutput().good_print("现在检测domain:%s是否有cdn" % domain)
    has_cdn = 0
    # ns记录和mx记录一样,都要查顶级域名,eg.dig +short www.baidu.com ns VS dig +short baidu.com ns
    result = get_string_from_command("dig ns %s +short" % get_root_domain(domain))
    pattern = re.compile(
        r"(cloudflare)|(cdn)|(cloud)|(fast)|(incapsula)|(photon)|(cachefly)|(wppronto)|(softlayer)|(incapsula)|(jsdelivr)|(akamai)", re.I)
    cloudflare_pattern = re.compile(r"cloudflare", re.I)
    if re.search(pattern, result):
        if re.search(cloudflare_pattern, result):
            print("has_cdn=1 from ns,and cdn is cloudflare")
            return {'has_cdn': 1, 'is_cloud_flare': 1}
        else:
            print("has_cdn=1 from ns")
            return {'has_cdn': 1, 'is_cloud_flare': 0}
    else:
        # 下面通过a记录个数来判断,如果a记录个数>1个,认为有cdn
        result = get_string_from_command("dig a %s +short" % domain)
        find_a_record_pattern = re.findall(r"((\d{1,3}\.){3}\d{1,3})", result)
        if find_a_record_pattern:
            ip_count = 0
            for each in find_a_record_pattern:
                ip_count += 1
            if ip_count > 1:
                has_cdn = 1
                return {'has_cdn': 1, 'is_cloud_flare': 0}
    return {'has_cdn': 0, 'is_cloud_flare': 0}


def get_domain_actual_ip_from_phpinfo(domain):
    # 从phpinfo页面尝试获得真实ip
    CLIOutput().good_print("现在尝试从domain:%s可能存在的phpinfo页面获取真实ip" % domain)
    phpinfo_page_list = ["info.php", "phpinfo.php", "test.php", "l.php"]
    http_or_https = get_http_or_https(domain)
    for each in phpinfo_page_list:
        url = http_or_https + "://" + domain + "/" + each
        CLIOutput().good_print("现在访问%s" % url)
        visit = get_request(url)
        code = visit['code']
        content = visit['content']
        pattern = re.compile(r"remote_addr", re.I)
        if code == 200 and re.search(pattern, content):
            print(each)
            actual_ip = re.search(r"REMOTE_ADDR[^\.\d]+([\d\.]{7,15})[^\.\d]+", content).group(1)
            return actual_ip
    # return 0代表没有通过phpinfo页面得到真实ip
    return 0


def flush_dns():
    # 这个函数用来刷新本地dns cache
    # 要刷新dns cache才能让修改hosts文件有效
    CLIOutput().good_print("现在刷新系统的dns cache")
    command = "/etc/init.d/dns-clean start && /etc/init.d/networking force-reload"
    os.system(command)


def modify_hosts_file_with_ip_and_domain(ip, domain):
    # 这个函数用来修改hosts文件
    CLIOutput().good_print("现在修改hosts文件")
    exists_domain_line = False
    with open("/etc/hosts", "r+") as f:
        file_content = f.read()
    if re.search(r"%s" % domain.replace(".", "\."), file_content):
        exists_domain_line = True
    if exists_domain_line == True:
        os.system("sed -ri 's/.*%s.*/%s    %s/' %s" % (domain.replace(".", "\."), ip, domain, "/etc/hosts"))
    else:
        os.system("echo %s %s >> /etc/hosts" % (ip, domain))


def check_if_ip_is_actual_ip_of_domain(ip, domain):
    # 通过修改hosts文件检测ip是否是domain对应的真实ip
    # 如果是则返回True,否则返回False
    CLIOutput().good_print("现在通过修改hosts文件并刷新dns的方法检测ip:%s是否是domain:%s的真实ip" % (ip, domain))
    from exp10it import get_request
    http_or_https = get_http_or_https(domain)
    domain_content = get_request(domain)['content']
    print(domain_content)
    os.system("cp /etc/hosts /etc/hosts.bak")
    modify_hosts_file_with_ip_and_domain(ip, domain)
    flush_dns()
    ip_content = get_request(http_or_https + "://%s" % ip)['content']
    os.system("rm /etc/hosts && mv /etc/hosts.bak /etc/hosts")
    if domain_content == ip_content:
        return True
    else:
        return False


def get_c_80_443_list(ip):
    # 得到ip的整个c段的开放80端口和443端口的ip列表
    CLIOutput().good_print("现在进行%s的c段开了80和443端口机器的扫描" % ip)
    nmap_command = "nmap %s/24 -p80,443 -Pn > /tmp/nmap.out" % (ip)
    os.system(nmap_command)
    with open("/tmp/nmap.out", "r+") as f:
        strings = f.read()
    import re
    _80_list = []
    _443_list = []
    open_80_matched = re.findall(
        r"Nmap scan .*\D(([0-9]{1,3}\.){3}[0-9]{1,3})\nHost is up..*\nPORT.*\n80/tcp\s+open", strings)
    open_443_matched = re.findall(
        r"Nmap scan .*\D(([0-9]{1,3}\.){3}[0-9]{1,3})\nHost is up..*\nPORT.*\n443/tcp\s+open", strings)
    if open_80_matched:
        for each in open_80_matched:
            _80_list.append(each[0])
    if open_443_matched:
        for each in open_443_matched:
            _443_list.append(each[0])
    return_value = {'_80_list': _80_list, '_443_list': _443_list}
    return return_value


def check_if_ip_c_machines_has_actual_ip_of_domain(ip, domain):
    # 检测ip的c段有没有domain的真实ip,如果有则返回真实ip,如果没有则返回0
    CLIOutput().good_print("现在检测ip为%s的c段中有没有%s的真实ip" % (ip, domain))
    from exp10it import get_http_or_https
    http_or_https = get_http_or_https(domain)
    print('domain的http或https是:%s' % http_or_https)
    ip_list = get_c_80_443_list(ip)
    _80_ip_list = ip_list['_80_list']
    _443_ip_list = ip_list['_443_list']
    domain_content = get_request(http_or_https + "://" + domain)['content']
    if http_or_https == "http":
        target_list = _80_ip_list
        print("c段开放80端口的机器列表:")
    else:
        target_list = _443_ip_list
        print("c段开放443端口的机器列表:")
    print(target_list)
    for each_ip in target_list:
        if True == check_if_ip_is_actual_ip_of_domain(each_ip, domain):
            return each_ip
    return 0


def get_ip_from_mx_record(domain):
    # 从mx记录中得到ip列表,尝试从mx记录中的c段中找真实ip
    print("尝试从mx记录中找和%s顶级域名相同的mx主机" % domain)
    import socket
    # domain.eg:www.baidu.com
    from exp10it import get_root_domain
    root_domain = get_root_domain(domain)
    from exp10it import get_string_from_command
    result = get_string_from_command("dig %s +short mx" % root_domain)
    sub_domains_list = re.findall(r"\d{1,} (.*\.%s)\." % root_domain.replace(".", "\."), result)
    ip_list = []
    for each in sub_domains_list:
        print(each)
        ip = socket.gethostbyname_ex(each)[2]
        if ip[0] not in ip_list:
            ip_list.append(ip[0])
    return ip_list


def check_if_mx_c_machines_has_actual_ip_of_domain(domain):
    # 检测domain的mx记录所在ip[或ip列表]的c段中有没有domain的真实ip
    # 有则返回真实ip,没有则返回0
    CLIOutput().good_print("尝试从mx记录的c段中查找是否存在%s的真实ip" % domain)
    ip_list = get_ip_from_mx_record(domain)
    if ip_list != []:
        for each_ip in ip_list:
            result = check_if_ip_c_machines_has_actual_ip_of_domain(each_ip, domain)
            if result != 0:
                return result
            else:
                continue
    return 0


def get_ip_value_from_online_cloudflare_interface(domain):
    # 从在线的cloudflare查询真实ip接口处查询真实ip
    # 如果查询到真实ip则返回ip值,如果没有查询到则返回0
    CLIOutput().good_print("现在从在线cloudflare类型cdn查询真实ip接口尝试获取真实ip")
    url = "http://www.crimeflare.com/cgi-bin/cfsearch.cgi"
    post_data = 'cfS=%s' % domain
    content = post_request(url, post_data)
    findIp = re.search(r"((\d{1,3}\.){3}\d{1,3})", content)
    if findIp:
        return findIp.group(1)
    return 0


def get_actual_ip_from_domain(domain):
    # 尝试获得domain背后的真实ip,前提是domain有cdn
    # 如果找到了则返回ip,如果没有找到返回0
    CLIOutput().good_print("进入获取真实ip函数,认为每个domain都是有cdn的情况来处理")
    import socket
    has_cdn_value = domain_has_cdn(domain)
    if has_cdn_value['has_cdn'] == 1:
        CLIOutput().good_print("检测到domain:%s的A记录不止一个,认为它有cdn" % domain)
        pass
    else:
        CLIOutput().good_print("Attention...!!! Domain doesn't have cdn,I will return the only one ip")
        true_ip = socket.gethostbyname_ex(domain)[2][0]
        return true_ip
    # 下面尝试通过cloudflare在线查询真实ip接口获取真实ip
    if has_cdn_value['is_cloud_flare'] == 1:
        ip_value = get_ip_value_from_online_cloudflare_interface(domain)
        if ip_value != 0:
            return ip_value
        else:
            pass
    # 下面尝试通过可能存在的phpinfo页面获得真实ip
    ip_from_phpinfo = get_domain_actual_ip_from_phpinfo(domain)
    if ip_from_phpinfo == 0:
        pass
    else:
        return ip_from_phpinfo
    # 下面通过mx记录来尝试获得真实ip
    result = check_if_mx_c_machines_has_actual_ip_of_domain(domain)
    if result == 0:
        pass
    else:
        return result
    print("很遗憾,在下认为%s有cdn,但是目前在下的能力没能获取它的真实ip,当前函数将返回0" % domain)
    return 0


def main(domain):
    actual_ip = get_actual_ip_from_domain(domain)
    if actual_ip != 0:
        print("恭喜,%s的真实ip是%s" % (domain, actual_ip))

if __name__ == '__main__':
    import sys
    import re
    import os
    domain = sys.argv[1]
    main(domain)
