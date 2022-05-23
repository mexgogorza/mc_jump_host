# mc_jump_host
Modern Client automate connection through jump host. It works for your current sessions, or with a default session to jump server
If using netcsl, remember to choose GSSAPI as first Authentication method

## SecureCRT_jump_host.py

* Connection Name: target-host
* SSH Hostname: jump-host
* Save this file to your machine
* In Logon Actions:
  * Check Logon script, and set the file location
  * Disable Automate Logon, in case it was enabled
* Copy & Paste Session, then change name to connect to a different host


## SecureCRT_jump_host_default_session.py

* Connection Name: jump-host
* SSH Hostname: jump-host
* Save this file to your machine
* In Logon Actions, check Login script
* set the file location
