#include <stdio.h>

void cubic(int *a, int *b)
{
    *a *= *a * *a;
    *b *= *b * *b;
}

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    cubic(&a, &b);
    printf("%d %d", a, b);
}