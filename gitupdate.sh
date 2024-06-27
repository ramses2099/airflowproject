#!/bin/bash
#
# This script updates git repo auto.
#

USER="ramses2099"
REPONAME="airflowproject"
DATE=`date +%d-%m-%y`
clear
echo $DATE
echo "Cheking status repo [ $REPONAME ] of user [ $USER ] ..."
git status
git add .
git commit -m "This is a commit changes repo $REPONAME "
git push
echo "Repo [ $REPONAME ] Update Successfully ..."