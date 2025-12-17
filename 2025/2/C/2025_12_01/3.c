#include <stdio.h>

void addN(int *p, int n)
{
    *p += n;
}

int main()
{
    int a = 3;
    addN(&a, 3);
    printf("%d", a);
}