#include <stdio.h>

int is_leap(int year)
{
    if (year % 400 == 0)
    {
        return 1;
    }
    if (year % 100 == 0)
    {
        return 0;
    }
    if (year % 4 == 0)
    {
        return 1;
    }
    return 0;
}

int main() {
    int birth_year;
    int total_days = 0;

    scanf("%d", &birth_year);

    for (int i = birth_year; i <= 2030; i++)
    {
        total_days += 365 + is_leap(i);
    }

    printf("%d", total_days);
}