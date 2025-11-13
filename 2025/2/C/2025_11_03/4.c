#include <stdio.h>
#define SIZE 5
int main()
{
    int arr[SIZE];

    for(int i = 0; i < SIZE; i++)
    {
        scanf("%d", &arr[i]);
    }

    for(int i = SIZE - 1; i >= 0; i--)
    {
        printf("%d \n", arr[i]);
    }

}