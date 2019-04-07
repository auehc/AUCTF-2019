#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:8002,reuseaddr,fork EXEC:python /pwn/pwn3.py,stderr" - simpleuser;
done
