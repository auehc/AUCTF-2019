#include <stdio.h>

int main()
{
    setvbuf(stdout, _IONBF, 0, 0);
    char flag[] = "nah this isnt it";
    char buffer[100];
    char test[] = "aubie{ch3ck_y0ur_pr1n7_p4r4m5}";
    char another[] = "are you looking for the flag?";
    printf("Hello welcome to my program! It doesn\'t do much. But it can read your input!\n");
    printf("Type something and I'll say it back!\n");
    fgets(buffer, 100, stdin);
    printf("You typed: ");
    printf(buffer);

    return 0;
}