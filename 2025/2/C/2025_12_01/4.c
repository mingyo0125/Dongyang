#include <stdio.h>

void tozero(int *start_pointer, int count)
{
    while (count -- >= 1)
    {
        *(start_pointer + count) = 0;
    }
}


int main()
{
    int aa[] = {1,3,5,7,9};
    int size = sizeof(aa) / sizeof(int);
    tozero(&aa[2],2);
    for(int i = 0; i < size; i++)
    {
        printf("%d, ", aa[i]);
    }
}