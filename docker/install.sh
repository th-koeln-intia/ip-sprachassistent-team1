#!/bin/bash

if [[ "$EUID" -ne 0 ]]
  then echo "Please run as root"
  exit
fi

raspi-config nonint do_spi 0
timedatectl set-timezone Europe/Berlin
apt-get -y update
apt-get -y upgrade
apt-get install -y git libffi-dev libssl-dev python3 python3-pip
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
usermod -aG docker pi
pip3 -v install docker-compose
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
./install.sh --compat-kernel
cp ./conf/asound.conf > /etc/asound.conf

echo "Please reboot to apply changes"
