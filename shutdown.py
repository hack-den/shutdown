import platform
import os
import subprocess

p = platform.system()

shutdown_dict = {
	"Linux" : "systemctl poweroff -i",
	"Windows" : "shutdown /s /t 00",
}

if p in shutdown_dict.keys() :
	os.system(shutdown_dict[p])

elif p == 'Darwin':
	subprocess.call(['osascript', '-e',
	'tell app "System Events" to shut down'])
