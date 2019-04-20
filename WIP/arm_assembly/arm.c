#include <stdio.h>
int main()
{
    //
    int a = 24;
    int b = 13;
    int i;
    int c;
    for (i = 1; i <= 24; i++)
    {
        a *= i;
        b += i;
        a += b;
    }
    //printf("%d", i);
    if (i == 1)
    {
        a += 2;
        b -= 10;
    }
    else if (i < 20)
    {
        a += 20;
        b += 222;
    }
    else if (i >= 20)
    {
        a += 80;
        b *= 80;
    }

    c = a - b;
    return c;
}