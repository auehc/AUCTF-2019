#!/bin/bash

echo This is a simple challenge
read input
touch ex
echo $input > ex
chmod +x ex
./ex
