#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $(realpath $0)))
cd $ROOT_PATH

handsdown -o docs_local --cleanup $@
handsdown --gh-pages `git config --get remote.origin.url` --cleanup $@
