#include <stdio.h>
#define PI 3.14

int main()
{
    const float radius = 5.37f;

    printf("원 반지름: %f", radius);
    printf("\n");
    printf("원 면적: %f", radius * radius * PI);
    printf("\n");
    printf("원 둘레: %f", 2 * PI * radius);
}