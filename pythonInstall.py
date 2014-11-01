'''
Python install script Version 2
'''

import subprocess as sp
from os import *
from time import *
import sys


py_ver = sys.version_info
print("Detected Python version {}".format(".".join(map(str, py_ver))))

if py_ver >= (2, 7):

	print("You have Python Installed Proceeding to system update!")
		
	sleep(5)
	sp.call("sudo apt-get update", shell = True)
	sp.call("sudo apt-get upgrade", shell = True )
	sp.call("sudo apt-get install python-dev", shell = True)
	sp.call("sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose", shell = True)
	sp.call("sudo apt-get install libboost-all-dev libusb-1.0-0-dev python-cheetah doxygen python-docutils", shell = True)
	sp.call("sudo add-apt-repository ppa:webupd8team/sublime-text-2", shell = True)
	sp.call("sudo apt-get update", shell = True)
	sp.call("sudo apt-get install sublime-text", shell = True)
	print("------------ Setup complete --------------")
			
else:

	sp.call("sudo apt-get update", shell = True)
	sp.call("sudo apt-get upgrade", shell = True)
	sp.call("cd $home", shell = True)
	sp.call("cd Downloads", shell = True)
	sp.call("echo Installing Python", shell = True)
	sleep(3)
	sp.call("wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tgz", shell = True)
	sp.call("tar -xvf Python-2.7.6.tgz", shell = True)
	sp.call("./configure", shell = True)
	sp.call("make", shell = True)
	sp.call("sudo make install", shell = True)
	sp.call("sudo apt-get install python-dev", shell = True)
	sp.call("sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose", shell = True)
	sp.call("sudo apt-get install libboost-all-dev libusb-1.0-0-dev python-cheetah doxygen python-docutils", shell = True)
	sp.call("sudo add-apt-repository ppa:webupd8team/sublime-text-2", shell = True)
	sp.call("sudo apt-get update", shell = True)
	sp.call("sudo apt-get install sublime-text", shell = True)
	sp.call("sudo apt-get install python-mpi4py", shell = True)
	print("------------ Setup complete --------------")
