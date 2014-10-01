#!/usr/bin/python2
#!/usr/bin/env python

#Author: Adeyin Ikpah
#Python Install script

from subprocess import *
from os import *
from time import *

call("sudo apt-get update", shell = True)
call("sudo apt-get upgrade", shell = True)
call("cd $home", shell = True)
call("cd Downloads", shell = True)
call("echo Installing Python", shell = True)
sleep(3)
call("wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tgz", shell = True)
call("tar -xvf Python-2.7.6.tgz", shell = True)
call("cd Python-2.7.6", shell = True)
call("./configure", shell = True)
call("make", shell = True)
call("sudo make install", shell = True)
call("sudo apt-get install python-dev", shell = True)
call("sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose", shell = True)
call("sudo apt-get install libboost-all-dev libusb-1.0-0-dev python-cheetah doxygen python-docutils", shell = True)
call("sudo add-apt-repository ppa:webupd8team/sublime-text-2", shell = True)
call("sudo apt-get update", shell = True)
call("sudo apt-get install sublime-text", shell = True)
