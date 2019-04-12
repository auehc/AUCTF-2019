# Print me some values

## Solution
printf() is vulnerable to injections. If you tell it to print %p and printf does not have any values to format with it will just print the next addresses available on the stack.

## Flag
aubie{ch3ck_y0ur_pr1n7_p4r4m5}