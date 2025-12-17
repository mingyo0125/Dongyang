#include <stdio.h>

void fuc(int *a, int *b, int *c)
{
    if(*a < 0)
    {
        *a = 0;
    }
    if(*b < 0)
    {
        *b = 0;
    }
    if(*c < 0)
    {
        *c = 0;
    }
}

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    fuc(&a,&b,&c);

    printf("%d %d %d", a, b, c);
}