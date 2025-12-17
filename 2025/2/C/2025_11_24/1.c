#include <stdio.h>

int tripleValue(int a)
{
    return a * 3;
}

int* triplePointer1(int *a)
{
    return *a * 3;
}

int main()
{
    int a = 3;

    printf("%d\n", tripleValue(a));
    printf("%d\n", triplePointer1(&a));
}