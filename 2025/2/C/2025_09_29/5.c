#include <stdio.h>

int main()
{
    char a;
    scanf("%c", &a);
    
    for(int i = 7; i >= 0; i--)
    {
        int mask = a << i;
        if (a & mask)
        {
            printf("1");
        }
        else
        {
            printf("0");
        }
    }
}