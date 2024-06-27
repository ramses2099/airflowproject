#!/bin/bash
#
# This script updates git repo auto.
#

USER="ramses2099"
REPONAME="airflowproject"
NOW = $(date '+%Y-%m-%d %H:%M:%S')
clear
echo "$NOW Cheking status repo [ $REPONAME ] of user [ $USER ] ..."
git status
git add .
git commit -m "This is a commit changes repo $REPONAME  date  $NOW "
git push
echo "Repo [ $REPONAME ] Update Successfully ..."