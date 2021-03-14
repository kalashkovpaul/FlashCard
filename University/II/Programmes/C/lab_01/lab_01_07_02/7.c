// Лаб. работа 1, Задача 7
// Автор: Калашков Павел ИУ7-26Б, Вариант 8, вариант задачи 2

#include <stdio.h>
#include <math.h>

double sx(double x, double eps)
// вычисление значений функции s(x) с точностью eps
{
	double result = 0, iteration = x; // результат, значение итерации
	int i = 1;
	while (fabs(iteration) > eps)
	{
		result += iteration;
		iteration = iteration * x * x * i * i / (i + 1) / (i + 2);
		i += 2;
	}
	return result;
}

int main(void)
{
	int in;
	double x, eps, f, s, delta, deltabig;
	in = scanf("%lf%lf", &x, &eps);
	if ((in != 2) || (eps < 0) || (eps > 1) || (fabs(x) <= 1e-10) || (fabs(x) > 1))
	{
		printf("Ошибка найдена \n");
		return -1;
	}
	f = asin(x);
	s = sx(x, eps);
	deltabig = fabs(f - s);	
	delta = deltabig / fabs(f);
	printf("%g \n", f);
	printf("%g \n", s);
	printf("%g \n", deltabig);
	printf("%g \n", delta);
	return 0;
}

	
