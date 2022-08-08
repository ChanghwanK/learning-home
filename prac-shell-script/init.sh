#!/bin/bash

export GITHUB_BRANCH="main"
stage=$GITHUB_BRANCH

if [ "$stage" == "main" ]; then
  echo main
elif [ "$stage" == "dev" ]; then
  echo dev
fi
  echo Path Setting Done
