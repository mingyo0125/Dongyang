#include <stdio.h>
#define SIZE 1
int main()
{
    char arr[SIZE];

    for(int i = 0; i < SIZE; i++)
    {
        scanf("%c", &arr[i]);
    }

    for(int i = 0; i < SIZE; i++)
    {
        if(arr[i] > 65)
        {
            arr[i] -= 32;
        }
        
        printf("%c", arr[i]);
    }

}