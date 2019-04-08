#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <iostream>

using namespace std;

int main()
{
    int i = 0;
    char blah[2];
    char test[] = "ooooooooooooooooooooo";

    strcpy(blah, test);
    printf("Hello Welcome to my Program!\n");
    printf("Not much happens here!\n");
    printf("What is your name?\n");
    return 0;
}