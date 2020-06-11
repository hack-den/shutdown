import platform
import os
import subprocess

p = platform.system()

if p == 'Linux':
	os.system('systemctl poweroff -i')

elif p == 'Windows':
	os.system('shutdown /s /t 00')

elif p == 'Darwin':
	subprocess.call(['osascript', '-e',
	'tell app "System Events" to shut down'])
