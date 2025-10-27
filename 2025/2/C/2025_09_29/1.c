#include <stdio.h>

int main()
{
    double a, b;
    scanf("%lf %lf", &a, &b);

    int result = (int)a * (int)b;
    printf("%d", result);
}