#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:8006,reuseaddr,fork EXEC:./pwn/pwn7,stderr" - simpleuser;
done
