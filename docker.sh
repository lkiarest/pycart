#!/bin/bash

envtype=$1
setting_file=settings.dev.py
nettype=host

if [ "$envtype" == "prod" ]; then
  setting_file=settings.prod.py
  nettype=bridge
fi

# build image
echo building image ...
sudo docker build --build-arg SETTING_FILE=$setting_file -t pycart .

# start container
echo start container ...
sudo docker run -d --name pycart --net $nettype -p 8080:8080  pycart
echo container started. visit http://localhost:8080
