# Beam Me Up Scotty

## Solution
Looking at the binary you can see that we are using strcpy which is vulnerable to BOF. We also see later we are calling a local variable which can be overriden. 

Overriding the variable with a function address we can arbitrarily call functions.

Looking around we see that hidden in printf is the flag

## Flag
aubie{ch3ck_y0ur_p4773rn_buff3r5}