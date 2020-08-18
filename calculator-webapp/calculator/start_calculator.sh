#!/bin/ash

/calculator/cpp/src/create_cpp.sh

python3.8 -m pip install -r /calculator/django/requirements.txt
cd /calculator/django/
python3.8 manage.py runserver 0.0.0.0:8000