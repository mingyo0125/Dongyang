#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int arr[] = {1,3,5,7,9};
    int size = sizeof(arr) / sizeof(int);
    for(int i = 0; i < size / 2; i++)
    {
        swap(&arr[i], &arr[size -1 - i]);
    }

    for(int i = 0; i < size; i++)
    {
        printf("%d", arr[i]);
    }
}