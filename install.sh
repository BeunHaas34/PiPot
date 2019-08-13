#!/bin/bash
# Disable IPV, due to bug with pip
echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf
sudo sysctl -p

echo "APT installing dependencies"
sudo apt-get --yes install build-essential git libnl-genl-3-dev libssl-dev python3 python3-pip python3-venv

echo "installing hostapd"
git clone https://github.com/sensepost/hostapd-mana
cd hostapd-mana
make -C hostapd
cd ..

echo "Installing PiPot"
# TODO Change branch
git clone https://github.com/TheHell34/PiPot.git -b develop PiPot
cd PiPot
echo "Creating venv"
python3 -m venv venv
echo "pip install"
sudo ./venv/bin/pip3 install -r requirements.txt

sudo chmod +x run.sh
sudo ./run.sh


