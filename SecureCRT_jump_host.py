# $language = "python"
# $interface = "1.0"

# Jump Host Script 
# This script is intended to ssh from current host to 
# host listed in the session name
# it uses the last portion of the Session Path as SSH Target
import SecureCRT


def main():
	objTab = crt.GetScriptTab()
	objTab.Screen.Synchronous = True
	strSessionPath = crt.Session.Path.replace("\\", "/")
	#crt.Dialog.MessageBox("name: " + strSessionPath)
	strSessionName = strSessionPath.split("/")[-1]
  #Ask for Username
	strUserName = crt.Dialog.Prompt("Enter Username here:","USERNAME","",False)
    #crt.Dialog.MessageBox("name: " + strSessionName)
  #Below string should be replaced for the correct prompt of the jump server used, this case is for netcsl002
	objTab.Screen.WaitForString("4.2$ ")
	objTab.Screen.Send("ssh " + strUserName +"@" + strSessionName + "\n")

main()
