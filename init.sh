#!/bin/sh

# Recommand autoenv 
# If you aren't autoenv user 
# execute this command line that '$ source PROJECT_HOME/.env'

source `pwd` .env

pyenv install 3.4.3

pyenv virtualenv 3.4.3 $PROJECT_NAME

ln -s `pyenv root`/versions/$PROJECT_NAME $PROJECT_HOME/$PROJECT_NAME

pyenv shell $PROJECT_NAME
pip install --upgrade pip

