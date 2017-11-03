#!/bin/bash

function test_python_script () {
    echo $1 "test start"
    ~/.pyenv/versions/3.5.1/bin/python $1
}
export -f test_python_script

SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd $SCRIPT_DIR

# find $SCRIPT_DIR -name "*.py" -type f | xargs -I{} echo {}
# find $SCRIPT_DIR -name "*spec.py" -type f | xargs -I{} test_python_script {}
find $SCRIPT_DIR -name "*spec.py" -type f | xargs -I % bash -c "test_python_script %"