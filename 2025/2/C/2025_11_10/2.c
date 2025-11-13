#include <stdio.h>

int CalcTax(int money)
{
    int taxPercent = 5;
    if(money >= 10000)
    {
        taxPercent = 10;
    }

    return money * (taxPercent * 0.01);
}

int main()
{
    int money;
    scanf("%d", &money);

    printf("%d", CalcTax(money));
}