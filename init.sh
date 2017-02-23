#!/bin/sh

# Recommand autoenv 
# If you aren't autoenv user 
# execute this command line
# when $ source PROJECT_HOME/.env

source `pwd` .env

pyenv install 3.4.3

pyenv virtualenv 3.4.3 $PROJECT_NAME_WEB
pyenv virtualenv 3.4.3 $PROJECT_NAME_IMAP

ln -s `pyenv root`/versions/$PROJECT_NAME_WEB $PROJECT_HOME/src/web/$PROJECT_NAME_WEB
ln -s `pyenv root`/versions/$PROJECT_NAME_IMAP $PROJECT_HOME/src/imap/$PROJECT_NAME_IMAP
