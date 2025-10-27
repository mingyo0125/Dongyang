#include <stdio.h>

int main()
{
    double height, weight;
    scanf("%lf %lf", &height, &weight);

    double bmi = weight / ((height * height) * 0.0001f);

    printf("%.1lf", bmi);
}