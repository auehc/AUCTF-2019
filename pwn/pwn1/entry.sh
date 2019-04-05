#!/bin/bash

while : 
do
    su -c "exec socat TCP-LISTEN:8000,reuseaddr,fork EXEC:/pwn/pwn1,stderr" - pwnuser;
done
