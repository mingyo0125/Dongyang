#include <stdio.h>
#include <stdlib.h>

#define ROWSIZE 3
#define COLSIZE 4
int main()
{
    int arr[ROWSIZE][COLSIZE];
    int sum = 0;

    for(int i = 0; i < ROWSIZE; i++)
    {
        for(int j = 0; j < COLSIZE; j++)
        {
            arr[i][j] = rand();
        }
    }

    for(int i = 0; i < ROWSIZE; i++)
    {
        for(int j = 0; j < COLSIZE; j++)
        {
            sum += arr[i][j];
        }
    }

    printf("%lf", sum / (ROWSIZE * COLSIZE));
}