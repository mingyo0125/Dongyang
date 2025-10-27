#include <stdio.h>

int main()
{
    int n = 4;
    int sum = n;

    while (n > 1)
    {
        n -= 1;
        sum *= n; 
    }
    
    printf("%d", sum);
}