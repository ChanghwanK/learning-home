#!bin/bash

echo 'start setting'
export GITHUB_BRANCH="dev"

if [[ $GITHUB_BRANCH -eq "main" ]]; then
    echo "result >>> hello world!"
elif [[ $GITHUB_BRANCH -eq "dev" ]]; then
    echo "result >>> false"
fi  
    echo "Done"
