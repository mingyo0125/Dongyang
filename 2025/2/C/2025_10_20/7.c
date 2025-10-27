#include <stdio.h>


int main()
{
    int count = 0;
	for(int i = 1; 1 <= 4000; i++)
    {
        if ((i % 4 == 0 &&
		    i % 100 != 0)
		    ||
		    i % 400 == 0)
	    {       
		    count++;
	    }
    }

    printf("%d", count);
}