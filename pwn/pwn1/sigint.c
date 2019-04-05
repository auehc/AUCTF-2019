#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>

void sigsegv_handler(int sig)
{
    FILE *fptr = fopen("flag.txt", "r");
    if (fptr == NULL)
    {
        printf("Too bad the flag is only located on the server!\n");
        exit(0);
    }
    char ch = fgetc(fptr);
    while (ch != EOF)
    {
        printf("%c", ch);
        ch = fgetc(fptr);
    }
    exit(1);
}

int main(int argc, char **argv)
{
    signal(SIGSEGV, sigsegv_handler);
    if (argc > 1)
    {
        char buf[32];
        strcpy(buf, argv[1]);

        printf("Thanks! Received: %s\n", buf);
    }
    else
    {
        printf("This program takes 1 argument.\n");
    }
    return 0;
}