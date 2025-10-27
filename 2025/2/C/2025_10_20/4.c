#include <stdio.h>

int main()
{
    int count = 0;
    for(int i = 1; i < 10000; i++)
    {
        if(i % 5 == 0 ||
           i % 7 == 0)
        {
            count++;
        }
    }

    printf("%d", count);
}