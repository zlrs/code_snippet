#!/bin/bash

# create test python script
touch run_time_test.py
echo "print('hello world')" > run_time_test.py

# method 1
a=`time(python run_time_test.py)`
echo $a

# method 2
b=$(time(python run_time_test.py))
echo $b

# a=="hello world"
# b=="hello world"
