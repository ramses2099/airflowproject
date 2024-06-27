#!/bin/bash
#
# This script check git repo status auto.
#

USER="ramses2099"
REPONAME="airflowproject"

clear
echo "Cheking status repo: $REPONAME of user: $USER ..."
git status
git pull
echo "Repo: $REPONAME Update Successfully ..."
sleep 5
clear