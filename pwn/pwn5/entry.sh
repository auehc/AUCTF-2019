#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:8004,reuseaddr,fork EXEC:python /pwn/pwn5.py,stderr" - simpleuser;
done
