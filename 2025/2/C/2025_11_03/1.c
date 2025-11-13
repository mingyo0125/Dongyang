#include <stdio.h>
#define SIZE 30
int main()
{
    int arr[SIZE];
    int sum = 0;
    for(int i = 0; i < SIZE; i++)
    {
        arr[i] = 3 * (i + 1);
    }

    for(int i = 0; i < SIZE; i++)
    {
        sum += arr[i];
    }

    printf("%d", sum);
}