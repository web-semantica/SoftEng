#!/bin/bash
#
# Purpose: Continuous deploy on staging enviroment
#
# Author: Victor Arnaud <victorhad@gmail.com>

sudo docker login --username $DOCKER_HUB_USER --password $DOCKER_HUB_PASS
sudo docker-compose -f docker-compose.staging.yml build
sudo docker-compose -f docker-compose.staging.yml push

# sudo apt-get install sshpass -y
# sshpass -p $SSH_PASSWORD ssh user@IP '/bin/bash /home/software/fga-ontology-deploy.sh'
