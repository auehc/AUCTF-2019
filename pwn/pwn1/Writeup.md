# Too Much!

## Solution
All this program does is read input from the input arguments, and it will copy said input using strcpy. Which is vulnerable to buffer overflow attacks.

The buffer at least 8 characters. So if you overload that the program will catch the seg fault and will then print out the flag.

## Flag
aubie{s1mpl3_b0f}

