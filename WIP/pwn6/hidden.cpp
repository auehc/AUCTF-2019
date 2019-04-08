#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <iostream>

using namespace std;
int printf(const char *format = NULL, ...)
{
    if (format == NULL)
    {
        printf("aubie{blahblah}\n");
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
    printf("aHR0cDovL2JpdC5seS9TVVBFUl9MT0dJTg==");
    return 0;
}

int secret()
{
    printf("bm90aGluZyBzcGVjaWFsIGhlcmUsIHNvcnJ5");
    return 0;
}

int main()
{
    volatile int (*fp)();

    char blah[4];

    char input[20];

    fp = 0;
    fgets(input, 20, stdin);
    strcpy(blah, input);
    printf("Take this, you might need it on your journey %p!\n", printf);

    if (fp)
    {
        printf("calling function pointer, jumping to 0x%x\n", fp);
        fp();
    }
}