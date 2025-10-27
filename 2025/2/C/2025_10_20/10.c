#include <stdio.h>
 
int main()
{
	int a = 1000000;
	int b;
	for (b = 1; b <= 10; b++)
	{
		printf("%2d년 : %.0lf원\n", b, a * (1 + 0.045 * b));
	}
}