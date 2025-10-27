#include <stdio.h>

int main()
{
    for(int i = 1; i <= 9; i++)
    {
        for(int j = 9; j >= i; j--)
        {
            prntf("%d", j);
        }
        printf("\n");
    }
    
}