#!/bin/bash

docker volume create --name="calculator-logs"
docker-compose -f prod_files/docker-compose.yml up
