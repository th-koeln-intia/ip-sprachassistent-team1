#!/bin/bash

# TODO Takes a very long time, is every command really necessary and can manual steps be stored here?

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
