#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, char** argv)                                                                  
{
    int c = 0;
    if (argc == 2){
        int a = atoi(argv[0]);
        int b = atoi(argv[1]);

        c = a * 2 + b *4;
    }

    return c;
}
