#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:1337,reuseaddr,fork EXEC:/simple/simple.sh,stderr" - simpleuser;
done
