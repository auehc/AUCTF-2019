#!/bin/bash
sysctl kernel.randomize_va_space=0
while :
do
	su -c "exec socat TCP-LISTEN:8005,reuseaddr,fork EXEC:/pwn/pwn6,stderr" - pwnuser;
done
