#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:7000,reuseaddr,fork EXEC:./rev/rev1,stderr" - simpleuser;
done
