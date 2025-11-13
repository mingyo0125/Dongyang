#include <stdio.h>

int isequalarray(int a[], int b[], int n)
{
	for (int i = 0; i < n; i++)
    {
		if (a[i] != b[i])
        {
            return 0;
        }
	}
	return 1;
}

int main(void)
{
	int a[] = { 4, 7, 9, 3, 6 };
	int b[] = { 4, 7, 9, 3, 6 };

	int sizea = sizeof(a) / sizeof(a[0]);
	int sizeb = sizeof(b) / sizeof(b[0]);

	if (isequalarray(a, b, sizea))
    {
		printf("두 배열은 같다.");
    }
	else
    {
		printf("두 배열은 다르다.");
    }
}