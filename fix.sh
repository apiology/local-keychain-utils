#!/bin/bash -e

# Get latest version from here: https://www.python.org/downloads/
python_version=3.7.0
pyenv install -s ${python_version:?}
pyenv virtualenv ${python_version:?} "$(cat .python-version)" || true
pip install --upgrade pip
pip install -r requirements_dev.txt
