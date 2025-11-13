#include <stdio.h>

int Sum(int a, int b)
{
    int start, end;
    if(a > b)
    {
        start = b;
        end = a;
    }
    else
    {
        start = a;
        end = b;
    }

    int sum = 0;

    for(int i = start; i <= end; i++)
    {
        sum += i;
    }

    return sum;
}

int main()
{
    int a, b;

    scanf("%d %d", &a, &b);

    printf("%d", Sum(a,b));
}