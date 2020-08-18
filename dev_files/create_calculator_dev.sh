#!/bin/bash

docker volume create --name="calculator-logs"
docker-compose -f dev_files/docker-compose-dev.yml up
