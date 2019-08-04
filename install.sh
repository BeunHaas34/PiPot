#!/bin/bash
# Disable IPV, due to bug with pip
echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf
sudo sysctl -p

# Check if Python3 is installed
if ! hash python3 && ! hash pip3 ; then
    echo "Installing Python3"
    sudo apt-get update
    sudo apt-get install python3 python3-pip
else
    echo "Python3 is installed"
fi

# Check is Hostapd is installed

if [ ! -f "./hostapd-mana/hostapd/hostapd" ] ; then
    echo "Installing hostapd"
    sudo apt-get update
    sudo apt-get install -f build-essential libssl-dev libnl-dev libnl-genl-3-dev -y
    git clone https://github.com/sensepost/hostapd-mana
    cd hostapd-mana
    make -C hostapd
else
    echo "Hostapd is installed"
fi

# Check if PiPot is installed
if [ ! -d "PiPot" ]; then
    echo "Installing PiPot"
    # TODO Change branch
    git clone https://github.com/TheHell34/PiPot.git -b develop PiPot
    cd PiPot
    echo "Creating venv"
    python3 -m venv venv
    echo "pip install"
    sudo ./venv/bin/pip3 install -r requirements.txt
else
    echo "PiPot is installed"
    cd PiPot
fi

sudo python3 manage.py runserver


