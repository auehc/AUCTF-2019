#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:7004,reuseaddr,fork EXEC:./rev/rev5,stderr" - simpleuser;
done
