#include <stdio.h>

int Max(int a, int b, int c)
{
    int max = a;
    if(b > max)
    {
        max = b;
    }
    if(c > max)
    {
        max = c;
    }

    return max;
}

int Min(int a, int b, int c)
{
    int min = a;
    if(b < min)
    {
        min = b;
    }
    if(c < min)
    {
        min = c;
    }

    return min;
}

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    printf("%d", Max(a,b,c) * Min(a,b,c));
}