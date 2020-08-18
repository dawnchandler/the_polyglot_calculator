#!/bin/bash

export COMPOSE_PROJECT_NAME="dschandl"
docker volume create --name="${COMPOSE_PROJECT_NAME}_calculator-logs"
docker-compose -f prod_files/docker-compose.yml up
