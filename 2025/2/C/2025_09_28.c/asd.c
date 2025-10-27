#include<stdio.h>

int main()
{
    int a, b;
    printf("두 정수를 입력하시오.\n");
    scanf("%d %d", &a, &b);
    printf("합 : %d + %d = %d\n", a, b, a + b);
    printf("평균 : %d + %d / 2 = %f\n", a, b, (a + b) / 2.0);
}