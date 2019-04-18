#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:8001,reuseaddr,fork EXEC:/pwn/pwn2,stderr" - pwnuser;
done
