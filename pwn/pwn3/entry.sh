#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:8003,reuseaddr,fork EXEC:python /pwn/pwn.py,stderr" - simpleuser;
done
