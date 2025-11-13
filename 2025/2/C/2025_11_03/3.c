#include <stdio.h>
#define SIZE 10
int main()
{
    int arr[SIZE];
    for(int i = 0; i < SIZE; i++)
    {
        scanf("%d", &arr[i]);
    }

    int max = arr[0];

    for(int i = 0; i < SIZE; i++)
    {
        if(max < arr[i])
        {
            max = arr[i];
        }
    }

    printf("%d", max);
}