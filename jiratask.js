// ==UserScript==
// @name         jira task
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  tampermonkey plugin for auto send task to workers
// @author       You
// @match        http://172.24.180.18:8080/secure/Dashboard.jspa
// @require      http://code.jquery.com/jquery-2.1.1.min.js
// @require      https://greasyfork.org/scripts/5392-waitforkeyelements/code/WaitForKeyElements.js?version=115012
// @grant        none
// ==/UserScript==

function find_url_baogaoren(url) {
    var uri_reg=/(\/browse.+)/g;
    var n1=uri_reg.exec(url);
    var uri=n1[1];
    var html="";
    $.ajax({
        type: "GET",
        url: uri,
        dataType: "html",
        async : false,
        success: function(data) {
            html=data;
        },
        error: function() {
            alert('Error occured');
        }
    });
    var baogaoren_reg=/<dt>报告人:<\/dt>[\s\S]+?<\/span><\/span>\s+([\s\S]+?)\s*?<\/span>/g;
    var m1=baogaoren_reg.exec(html);
    var baogaoren=m1[1];
    var details_reg=/<div id=description.+?>[\s\S]+?<p>([\s\S]+?)<\/div>/g;
    var m2=details_reg.exec(html);
    var details=m2[1];
    return [baogaoren,details];
}

function worker() {
    var issuetable=document.getElementById('gadget-12340').contentWindow.document.getElementById('issuetable');
    var framehtml=issuetable.innerHTML;
    var tr = /(<tr id="(\w+)"[\s\S]+?<\/tr>)/g;
    var m;
    while (m = tr.exec(framehtml)) {
        var issueitemhtml=m[1];
        var issueid=m[2];
        var keyvaluereg=eval("/"+'<tr id="'+issueid+'"[\\s\\S]+?<td class="summary"[\\s\\S]+?href="(.+)">(.+)<[\\s\\S]+?>安全测试<'+"/g");
        var n;
        while (n = keyvaluereg.exec(issueitemhtml)) {
            var link=n[1];
            var zhuti=n[2];
            $('#'+issueid+' > td.status > span',top.frames["gadget-12340"].document).css("color","red");
            $('#'+issueid+' > td.status > span',top.frames["gadget-12340"].document).click({'link':link,'zhuti':zhuti},add_task);
            function add_task(event){
                var _=find_url_baogaoren(event.data.link);
                var baogaoren=_[0];
                var details=_[1];
                //alert(baogaoren);
                //alert(details);
                $.ajax({
                    url: "http://python script server which will write job record to database:8888/",
                    type: "get",
                    crossDomain: true,
                    dataType: 'jsonp',
                    data: {
                        jira_url: event.data.link,
                        jira_zhuti: event.data.zhuti,
                        baogaoren: baogaoren,
                        details: details
                    },
                    success: function (response) {
                        alert(response.result);
                    },
                    error: function (response) {
                        alert(response.result);
                    }
                });
            }

        };
    }
}

var checkExist = setInterval(function() {
   if ($('#issuetable',top.frames["gadget-12340"].document).length) {
      worker();
      clearInterval(checkExist);
   }
}, 100); // check every 100ms

