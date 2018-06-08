#!/bin/bash
#
# Purpose: Continuous deploy on production enviroment
#
# Author: Victor Arnaud <victorhad@gmail.com>

sudo docker login --username $DOCKER_HUB_USER --password $DOCKER_HUB_PASS
python3 softeng/manage.py collectstatic
sudo docker-compose -f docker-compose.production.yml build
sudo docker-compose -f docker-compose.production.yml push

# sudo apt-get install sshpass -y
# sshpass -p $SSH_PASSWORD ssh user@IP '/bin/bash /home/software/softeng-deploy.sh'
