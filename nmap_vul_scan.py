import re
import os
import pdb
input("please generate two files: `users.lst` and `pass.lst` in current directory for brute scan,press any key to continue where it's ready...")
ip_range=input("please input your ip scan range in nmap format\n:>")
nmap_scan_cmd='nmap -T4 -A -v -Pn %s -p 21,22,23,25,80,443,445,1433,3306,3389,3690,5900,8080 -oN nmap_result.txt' % ip_range
print("executing `%s`" % nmap_scan_cmd)
os.system(nmap_scan_cmd)
nmap_result_abspath="nmap_result.txt"
with open(nmap_result_abspath,"r+") as f:
    nmap_result=f.read()
port_list=re.findall(r"(\d+)/tcp\s+",nmap_result)
port_list=list(set(port_list))
open_port_dict={}
for port in port_list:
    if port not in open_port_dict:
        open_port_dict[port]=[]
    all=re.findall(r"Nmap scan report for (\S+)\nHost is up.+\n+(.+\n)*%s/tcp\s+open.+\n(.+\n)*\n" % port,nmap_result)
    for item in all:
        ip=item[0]
        if ip not in open_port_dict[port]:
            open_port_dict[port].append(ip)
for port in open_port_dict:
    ip_list=open_port_dict[port]
    for ip in ip_list:
        with open("%s.txt" % port,"a+") as f:
            f.write(ip+"\n")
nmap_cmd_list=[
        'nmap -T insane --script ftp-brute.nse -p 21 -iL 21.txt -oN ftp-brute.txt -v',
        'nmap -T insane --script ssh-brute.nse --script-args userdb=users.lst,passdb=pass.lst -p 22 -iL 22.txt -oN ssh-brute.txt -v',
        'nmap -T insane --script telnet-brute.nse --script-args userdb=users.lst,passdb=pass.lst -p 23 -iL 23.txt -oN telnet-brute.txt -v',
        'nmap -T insane --script smtp-brute.nse -p 25 -iL 25.txt -oN smtp-brute.txt -v',
        'nmap -T insane --script smb-vuln-ms10-054.nse -p 445 -iL 445.txt -oN 10054.txt -v',
        'nmap -T insane --script smb-vuln-ms10-061.nse -p 445 -iL 445.txt -oN 10061.txt -v',
        'nmap -T insane --script smb-vuln-ms17-010.nse -p 445 -iL 445.txt -oN 17010.txt -v',
        'nmap -T insane --script ms-sql-brute.nse -p 1433 -iL 1433.txt -oN ms-sql-brute.txt -v',
        'nmap -T insane --script mysql-brute.nse -p 3306 -iL 3306.txt -oN mysql-brute.txt -v',
        'nmap -T insane --script rdp-vuln-ms12-020.nse -p 3389 -iL 3389.txt -oN 12020.txt -v',
        'nmap -T insane --script svn-brute.nse -p 3690 -iL 3690.txt -oN svn-brute.txt -v',
        'nmap -T insane --script realvnc-auth-bypass.nse -p 5900 -iL 5900.txt -oN realvnc-auth-bypass.txt -v',
        'nmap -T insane --script vnc-brute.nse -p 5900 -iL 5900.txt -oN vnc-bute.txt -v'
        ]
for cmd in nmap_cmd_list:
    print("\nexecuting `%s`\n" % cmd)
    os.system(cmd)
print("finished.")
