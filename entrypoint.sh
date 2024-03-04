#!/bin/bash

set -x

cd /home/ubuntu
sudo rm -rf erpnextdocker
sudo git clone https://oauth2:glpat-xGCtAGd4KtDyn-S1feRg@git@repo.innogenio.com:joshy.sunny/ig-frappe-docker.git -b development
cd erpnextdocker
sudo chmod +x deploy.sh
. deploy.sh
export public_ip=$(curl http://checkip.amazonaws.com)
echo "please use the following link to access your site - http://$public_ip:80 "
