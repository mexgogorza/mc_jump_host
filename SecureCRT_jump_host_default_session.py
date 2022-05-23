# $interface = "1.0"

# Jump Host Script for default session
# This script is intended to ssh from current host to 
# the one prompted using the username provided
# 
import SecureCRT


def main():
	#Set to True if you want to enable session login
	sessionLog = True
	logfilepath = "%temp%\\"
	
	objTab = crt.GetScriptTab()
	objTab.Screen.Synchronous = True
	#Ask for hostname of device to connect
	strSessionName = crt.Dialog.Prompt("Enter hostname here:","Hostname","",False)
	#Ask for Username
	strUserName = crt.Dialog.Prompt("Enter Username here:","Username","",False)
	#crt.Dialog.MessageBox("name: " + strSessionName)
	#Set the hostname as the Tab name
	objTab.Caption = strSessionName
  #if the session has logging enabled, will save a log to user temp folder usign hostname as filename
	if sessionLog:
		crt.Session.LogFileName =  logfilepath + strSessionName + ".log"
		crt.Dialog.MessageBox(crt.Session.LogFileName)	
		crt.Session.Log(sessionLog)
	objTab.Screen.WaitForString("4.2$ ")
	objTab.Screen.Send("ssh " + strUserName +"@" + strSessionName + "\n")

main()
