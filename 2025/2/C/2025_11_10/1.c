#include <stdio.h>

int volume(int w, int l, int h)
{
    return w * l * h;
}

int surface(int w, int l, int h)
{
    return (2 * w * l) + (2 * l * h) + (2 * w * h);
}

int main()
{
    int w, l, h;
    scanf("%d %d %d", &w, &l, &h);

    printf("%d", volume(w, l, h));
    printf("%d", surface(w, l, h));
}