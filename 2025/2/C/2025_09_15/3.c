#include <stdio.h>

int main()
{
    double galaxies = 2000.0;
    double stars_per_galaxy = 3500.0;

    double total_stars = galaxies * stars_per_galaxy;

    printf("총 별의 수: %.lf", total_stars);
    printf("억개");
    return 0;
}
