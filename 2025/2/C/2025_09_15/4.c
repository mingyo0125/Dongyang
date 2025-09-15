#include <stdio.h>

int main()
{
    const float yRate = 0.035f;
    float interest = 100000000 * (yRate / 12);

    printf("1억원의 한달 이자: %f", interest);
}