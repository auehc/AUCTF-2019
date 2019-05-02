#!/bin/bash

while :
do
    su -c "socat TCP4-listen:8007,reuseaddr,fork EXEC:/pwn/pwn8" - pwnuser
done
