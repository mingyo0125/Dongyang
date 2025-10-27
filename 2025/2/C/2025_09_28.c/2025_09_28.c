1
#include <stdio.h>

int main() 
{
    float meter, yard;

    printf("미터 값을 입력하세요: ");
    scanf_s("%f", &meter);

    yard = meter / 0.914;

    printf("%.2f 미터는 %.2f 야드입니다.\n", meter, yard);

    return 0;
}


2
#include<stdio.h>

int main()
{
	int y;
	double a;
	printf("입력받은 수를 5제곱 하시오.");
	scanf_s("%d", &y);
	a = y * y * y * y * y;
	printf("제곱한 수: %lf", a);
}


3
#include<stdio.h>

void main()
{
	int a, b, c;
	printf("가로 세로 높이를 입력!\n");
	scanf_s("%d &d &d", &a, &b, &c);
	int bupi = a * b * c;
	printf("부피: %d\n", bupi);
}


4
#include<stdio.h>
#define PI 3.14159

void main()
{
	int r;
	double area;
	printf("반기름을 입력하시오!\n");
	scanf_s("%d", &r);
	area = PI * r * r;
	printf("원의 넓이: %lf", area);
}


5
#include<stdio.h>

int main()
{
	int a, b, c, d, e;
	int f;
	printf("5개의 숫자를 입력하시오.\n");
	scanf_s("%d %d %d %d %d", &a, &b, &c, &d, &e);
	 f= a+b+c+d+e/5;
	printf("입력받은 숫자의 평균: %d", f);
}

6
#include<stdio.h>

int main()
{
	double c, f;
	printf("화씨 온도를 입력하세요.\n");
	scanf_s("%lf", &f);
	c = (f - 32) / 1.8;
	printf("입력받은 화씨를 섭씨로 전환하시오.%.2lf", c);
}

7
#include <stdio.h>
#define PI 3.141592653589793
#define SP(r) ((4.0/3.0) * PI * (r) * (r) * (r))

int main(void) {
    double earth_r = 6378.0; 
    double moon_r = 1737.0; 

    double earth_v = SP(earth_r);
    double moon_v = SP(moon_r);

    double diff = earth_v - moon_v;      
    double ratio = earth_v / moon_v;    

    printf("지구 부피: %.2f km^3\n", earth_v);
    printf("달 부피: %.2f km^3\n", moon_v);
    printf("부피 차이: %.2f km^3\n", diff);
    printf("지구는 달의 %.2f 배 크기\n", ratio);

    return 0;
}


8
#include<stdio.h>

int main()
{
	double a, b;
	double base, hei;
	double rect, tri;

	printf("두 실수를 입력: ");
	scanf_s("%lf %lf", &a, & b);

	if (a > b)
	{
		base = a;
		hei = b;
	}
	else {
		base = b;
		hei = a;
	}

	rect = base * hei;
	tri = rect / 2;
	printf("사각형의 면적:%12.3f\n", rect);
	printf("삼각형의 면적: %-12.3f\n", tri);


}


6
#include<stdio.h>

int main()
{
    int a, b;
    printf("두 정수를 입력하시오.\n");
    scanf("%d %d", &a, &b);
    printf("합 : %d + %d = %d\n", a, b, a + b);
    printf("평균 : %d + %d / 2 = %f\n", a, b, (a + b) / 2.0);
}