#!/bin/bash
echo 'Releasing new version of MONEI PYTHON SDK'
cd ..
rm -rf dist/*
python3 -m pip install --upgrade setuptools wheel twine
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/* -u MONEI
cd build
