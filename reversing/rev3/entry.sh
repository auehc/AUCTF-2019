#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:7002,reuseaddr,fork EXEC:./rev/rev3,stderr" - simpleuser;
done
