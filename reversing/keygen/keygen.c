#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

char *gen_key(const char *key)
{
    char *result = (char *)malloc(64);

    int length = strlen(key);
    unsigned char seed = 0x48;
    for (int i = 0; i < length; i++)
    {
        result[i] = 48 + (seed * key[i] + seed / 2) % 10;
        seed = result[i];
    }
    return result;
}

_Bool verify_key(char *key)
{
    if (strlen(key) < 8 || strlen(key) > 32)
    {
        return false;
    }
    char *result = gen_key(key);
    // random password: 02501799219856
    char *compare = "255067256325588";
    return !strcmp(compare, result);
}

int main()
{
    setvbuf(stdout, 0, _IONBF, 0);
    printf("\nPlease Enter a product key to continue: \n");
    char pkey[65];
    fgets((char *)pkey, 65, stdin);
    if (verify_key(pkey))
    {
        FILE *infile = fopen("flag.txt", "r");
        if (infile == NULL)
        {
            printf("Great Work! Too bad the flag is only on the server!\n");
            return 0;
        }
        char output[100];
        fgets(output, 100, infile);
        printf("%s", output);
    }
}
