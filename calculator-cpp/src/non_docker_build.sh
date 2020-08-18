#!/bin/bash

rm -fr ../build || true
python3.8 cpp-setup.py build
mv build ../.
