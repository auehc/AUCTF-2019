//this file should never make it to master, just used for my own testing.
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>

unsigned char globPass[25] = {'\x5c', '\x70', '\x7a', '\x74', '\x58', '\x65', '\x42', '\x7e', '\x1b', '\x00'};
unsigned char inputPass[25] = {};
bool passCheck();

unsigned char *check(unsigned char *func)
{
    //the check() function checks itself for the presence of breakpoints as well :)
    if (func != (unsigned char *)check)
    {
        if (check((unsigned char *)check) != (unsigned char *)check)
        {
            return NULL;
        }
    }
    unsigned char val = '\x99';
    unsigned char xorVal = '\x11';
    int i, j;
    unsigned char *p = func;
    //prints the first 64 bytes of the function
    for (j = 0; j < 4; j++)
    {
        //printf("\n%p: ",p);
        //iterate through lines of 16
        for (i = 0; i < 16; i++)
        {
            //this does nothing except help obfuscate how the key is hidden.
            xorVal += i * j;
            *p++;
            //printf("%.2x ", *p);
            //printf("%.2x ","\xcc");
            if ((*p ^ '\x55') == val)
            {
                //printf("Found a breakpoint\n");
                return NULL;
            }
            xorVal -= i * j;
        }
    }
    //if we get here, we can encrypt the input password since there are no breakpoints.
    // if we decrypt the input password
    for (int i = 0; i < sizeof(inputPass); i++)
    {
        if (func == (unsigned char *)passCheck)
        {
            if (inputPass[i] != '\x00')
            {
                inputPass[i] = inputPass[i] ^ xorVal; // 0x11
            }
            else
            {
                //do nothing
            }
        }
    }
    //Only gets here if no breakpoints
    return func;
}
bool passCheck()
{
    if (check((unsigned char *)passCheck) == (unsigned char *)passCheck)
    {
        //password = MakeItSo\n
        if (strcmp((char *)globPass, (char *)inputPass) == 0)
        {
            return true;
        }
        else
        {
            printf("\nWrong Password\n");
            return false;
        }
    }
    return false;
}

int main(int argc, char const *argv[])
{

    setvbuf(stdout, 0, _IONBF, 0);
    if (check((unsigned char *)main) == (unsigned char *)main)
    {
        printf("\nWelcome. Please Enter a password to continue: \n");
        char password[25];

        // gets user password and then copies it to the global variable
        fgets((char *)password, 25, stdin);
        strcpy((char *)inputPass, (char *)password);
        if (passCheck()) // if password is correct print flag
        {
            FILE *infile = fopen("flag.txt", "r");
            if (infile == NULL)
            {
                printf("Too bad the flag is only on the remote server!\n");
                return 0;
            }
            char output[100];
            fgets(output, 100, infile);
            printf(output);
        }
    }
    return 0;
}
