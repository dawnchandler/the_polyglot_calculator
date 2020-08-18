#!/bin/ash

cd /calculator/cpp/src/
rm -fr ../build | true
rm -fr build | true

python3.8 cpp-setup.py build
mv build ../.
cd -