#!/bin/bash
echo 'Releasing new version of MONEI PYTHON SDK'
python3 -m pip install --user --upgrade setuptools wheel twine
python3 ../setup.py sdist --dist-dir=../dist bdist_wheel --dist-dir=../dist
python3 -m twine upload ../dist/*
