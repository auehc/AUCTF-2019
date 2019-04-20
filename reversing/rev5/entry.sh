#!/bin/bash

while :
do
	su -c "exec socat TCP-LISTEN:7001,reuseaddr,fork EXEC:/rev/rev5,stderr" - revuser;
done
