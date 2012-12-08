import os
import psutil

print("I\'ll help you... soon...")

#PROCNAME = "python.exe"
PROCNAME = "Python"

def isEvil(arr):
	for item in arr:
		if item.find("Evil") != -1:
			return True		#EVIL!!!

	return False	#it's not Evil

for proc in psutil.process_iter():
    if proc.name == PROCNAME and isEvil(proc.cmdline) and proc.pid != os.getpid():
        print "I found child of evil - ", proc.cmdline
        proc.kill()