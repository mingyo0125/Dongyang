#include <stdio.h>
#define SIZE 10
 
int main()
{
    double arr[SIZE];
 
    for (int i = 0; i < SIZE; i++)
    {
        arr[i] = 1.0 / ((i + 2) * (i + 3));
        printf("%d/(%d*%d) = %lf\n", 1, i + 2, i + 3, arr[i]);
    }
 
}