#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:8001,reuseaddr,fork EXEC:/simple/pwn2,stderr" - simpleuser;
done
