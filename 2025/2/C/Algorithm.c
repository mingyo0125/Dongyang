#include <stdio.h>

int main()
{
    int arr[10] = {10};

    for(int i = 0; i < 10; i++)
    {
        printf("%d: %d\n", i, arr[i]);
    }

    fflush(stdout);
}