#!/usr/bin/python2
#!/usr/bin/env python


#GNU Radio Install script

from subprocess import *
from os import *
from time import *

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
call("echo Installing USRP Driver UHD", shell = True)
sleep(3)
call("sudo chmod u+x UHDDriver.sh", shell = True)
call("./UHDDriver.sh")
call("echo Installing Git", shell = True)
sleep(3)
call("sudo apt-get update", shell = True)
call("sudo apt-get install git", shell = True)
call("echo Installing cmake", shell = True)
sleep(3)
call("sudo apt-get install cmake", shell = True)
call("echo Installing boost", shell = True)
sleep(3)
call("sudo apt-get install libboost-all-dev", shell = True)
call("echo Installing cppunit", shell = True)
sleep(3)
call("sudo apt-get install libcppunit-dev:i386 libcppunit-doc libcppunit-dev", shell = True)
call("echo Installing fftw", shell = True)
sleep(3)
call("sudo apt-get install fftw-dev", shell = True)
call("echo Installing gsl", shell = True)
sleep(3)
call("sudo apt-get install libgsl0ldbl", shell = True)
call("echo Installing swig", shell = True)
sleep(3)
call("sudo apt-get install swig", shell = True)
call("echo Installing wxPython", shell = True)
sleep(3)
call("sudo apt-get install python-wxgtk2.8", shell = True)
call("echo Installing qt", shell = True)
sleep(3)
call("sudo apt-get install libqt4-core libqt4-gui", shell = True)
call("echo Installing qwt", shell = True)
sleep(3)
call("echo Installing pyqt", shell = True)
sleep(3)
call("sudo apt-get install python-qt4", shell = True)
call("echo Installing doxygen", shell = True)
sleep(3)
call("sudo apt-get install doxygen", shell = True)
call("echo Installing setuptools", shell = True)
sleep(3)
call("sudo apt-get install python-setuptools", shell = True)
call("echo Installing setuptools", shell = True)
sleep(3)
call("sudo apt-get install python-setuptools", shell = True)
call("sudo apt-get install build-essential xorg-dev libudev-dev libts-dev libgl1-mesa-dev libglu1-mesa-dev libasound2-dev libpulse-dev libopenal-dev libogg-dev libvorbis-dev libaudiofile-dev libpng12-dev libfreetype6-dev libusb-dev libdbus-1-dev zlib1g-dev libdirectfb-dev", shell = True)
call("echo Installing SDL", shell = True)
sleep(3)
call("wget http://www.libsdl.org/release/SDL2-2.0.3.tar.gz", shell = True)
call("sudo gzip -d SDL2-2.0.3.tar.gz", shell = True)
call("sudo tar -xvf SDL2-2.0.3.tar", shell = True)
call("cd SDL2-2.0.3", shell = True)
call("./configure",shell = True)
call("make", shell = True)
call("sudo make install", shell = True)
call("echo Installing GNURadio", shell = True)
sleep(3)
call("sudo apt-get install gnuradio", shell = True)
sleep(3)
call("sudo gnuradio-companion", shell = True)













