#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <iostream>
#include <stdio.h>

using namespace std;
int printf(const char *format = NULL, ...)
{
    if (format == NULL)
    {
        FILE *infile = fopen("flag.txt", "r");
        if (infile == NULL)
        {
            printf("Great Work! Too bad the flag is only on the server!\n");
            return 0;
        }
        char output[100];
        fgets(output, 100, infile);
        puts(output);
    }
    va_list arg;
    int done;

    va_start(arg, format);
    done = vfprintf(stdout, format, arg);
    va_end(arg);

    return done;
}

int test()
{
    printf("this is a test function!\n");
    return 0;
}

int f()
{
    return 0;
}

int l()
{
    return 0;
}

int a()
{
    return 0;
}

int g()
{
    return 0;
}

int a1234()
{
    FILE *infile = fopen("key.txt", "r");
    if (infile == NULL)
    {
        printf("Great Work! Too bad the flag is only on the server!\n");
        return 0;
    }
    char output[100];
    fgets(output, 100, infile);
    puts(output);
    return 0;
}

int secret()
{
    FILE *infile = fopen("secret.txt", "r");
    if (infile == NULL)
    {
        printf("Great Work! Too bad the flag is only on the server!\n");
        return 0;
    }
    char output[100];
    fgets(output, 100, infile);
    puts(output);
    return 0;
}

int main()
{
    volatile int (*fp)();
    setvbuf(stdout, NULL, _IONBF, 0);
    char copy[4];

    char input[20];
    printf("Welcome to Main my address is: %p\n", main);
    fp = 0;
    fgets(input, 20, stdin);
    strcpy(copy, input);

    if (fp)
    {
        printf("calling function pointer, jumping to %p\n", fp);
        fp();
    }
}