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
    char input[8];
    gets(input);

    printf("Thanks! Received: %s\n", input);

    return 0;
}