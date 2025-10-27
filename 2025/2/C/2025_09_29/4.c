#include <stdio.h>

int main()
{
    double a, b, c, d, e;

    scanf("%lf %lf %lf %lf %lf", &a, &b, &c, &d, &e);

    int iSum = (int)a + (int)b + (int)c + (int)d + (int)e;
    double dSum = (a - (int)a) + (b - (int)b) + (c - (int)c) + (d - (int)d) + (e - (int)e);

    printf("정수: %d\n소수: %lf", iSum, dSum);
}