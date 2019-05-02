#include <stdio.h>
#include <stdlib.h>

void print()
{
    char buf[64];
    printf("This is the address of buffer: %p\n", buf);
    gets(buf);
}

int main()
{
    setvbuf(stdout, _IONBF, 0, 0);
    print();
}
