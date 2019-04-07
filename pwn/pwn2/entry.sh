#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:8001,reuseaddr,fork EXEC:/simple/simple.sh,stderr" - simpleuser;
done
