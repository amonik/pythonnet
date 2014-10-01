#!/bin/bash
clear

echo "This will install UHD Driver"

sudo bash -c 'echo "deb http://files.ettus.com/binaries/uhd_unstable/repo/uhd/ubuntu/`lsb_release -cs` `lsb_release -cs` main" > /etc/apt/sources.list.d/ettus.list'
sudo apt-get update
sudo apt-get install -t `lsb_release -cs` uhd

echo "This will install qwt"
wget http://sourceforge.net/projects/qwt/files/qwt/6.1.0/qwt-6.1.0.tar.bz2/download
sudo bzip2 -d qwt-6.1.0.tar.bz2
tar -xvf qwt-6.1.0.tar
cd qwt-6.1.0/
qmake qwt.pro
make
sudo make install
