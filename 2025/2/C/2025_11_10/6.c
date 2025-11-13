#include <stdio.h>

int isPrime(int a)
{
    for(int i = 2; i < a; i++)
    {
        if(a % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int a;
    scanf("%d", &a);
    int primeNum = 0;
    for(int i = a - 1; i > 1; i--)
    {
        if(isPrime(i) == 1)
        {
            primeNum = i;
            break;
        }
    }

    printf("%d", primeNum);
}