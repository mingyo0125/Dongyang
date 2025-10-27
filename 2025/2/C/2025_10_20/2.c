#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);

    for(int i = 3; i <= a; i+=3)
    {
        printf("%d\n", i);
    }
    
}