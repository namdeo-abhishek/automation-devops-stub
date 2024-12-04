#!/bin/bash -xc
pip3 install -U pytest --no-warn-script
cd $HOME/$NAME
rm -rf repo
mkdir repo
cd repo
git init
rm -rf /tmp/git-remote-repo
mkdir -p /tmp/git-remote-repo
cd /tmp/git-remote-repo
git init --bare
cd $HOME/$NAME/repo
git remote add origin /tmp/git-remote-repo
