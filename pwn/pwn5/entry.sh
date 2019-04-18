#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:8004,reuseaddr,fork EXEC:/pwn/pwn5.py,stderr" - pwnuser;
done
