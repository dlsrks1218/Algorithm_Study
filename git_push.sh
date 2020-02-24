#!/bin/zsh

echo "git add ."
git add .
echo "git commit -m $0"
git commit -m $0
echo "git push -u origin master"
git push -u origin master
