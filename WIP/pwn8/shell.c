#include <stdio.h>
#include <stdlib.h>

int main()
{
    setvbuf(stdout, _IONBF, 0, 0);
    char buf[500];
    printf("Hello Welcome to my program! I've been programmed to print out the address of my buffer variable!\n");
    printf("Buffer: %p!\n", buf);
    gets(buf);
}