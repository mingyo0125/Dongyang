#include <stdio.h>

int maxValue(int *a, int *b, int *c)
{
    int max = *a;
    if(max < *b)
    {
        max = *b;
    }

    if(max < *c)
    {
        max = *c;
    }

    return max;
}

int main()
{
    int a = 10;
    int b = 20;
    int c = 30;

    printf("%d", maxValue(&a, &b, &c));
}