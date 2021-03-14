// Лаб. работа 1, задача №6
// Автор: Калашков П.А. ИУ7-26Б, Вариант 8, вариант задачи 2
#include <stdio.h>
#include <math.h>

int triangle(long *xa, long *ya, long *xb, long *yb, long *xc, long *yc, long *x0, long *y0)
{
	// через уравнение прямой
	long v = (((*x0 - *xa) * (*yb - *ya) - (*y0 - *ya) * (*xb - *xa)) * ((*xc - *xa) * (*yb - *ya) - (*yc - *ya) * (*xb - *xa)));
	if (v > 0)
		return 0;
	else if (v == 0)
		return 1;
	else
		return 2;
}
int main(void)
{
	/*
	printf("Определение принадлежности точки области внутри треугольника.\n");
	printf("0 - принадлежит;\n");
	printf("1 - лежит на границе;\n");
	printf("2 - лежит вне треугольника.\n");
	*/
	int ina, inb, inc, in0; // переменные для проверки ввода, для ответа
	long xa, ya, xb, yb, xc, yc, x0, y0, v1, v2, v3; // переменные для координат
	// printf("Введите координаты точки А: ");
	ina = scanf("%ld%ld", &xa, &ya);
	// printf("Введите координаты точки B: ");
	inb = scanf("%ld%ld", &xb, &yb);
	// printf("Введите координаты точки С: ");
	inc = scanf("%ld%ld", &xc, &yc);
	// printf("Введите координаты точки М (основной точки): ");
	in0 = scanf("%ld%ld", &x0, &y0);
		
	if ((ina != 2) || (inb != 2) || (inc != 2) || (in0 != 2))
	{
		printf("Ввод неверен");
		return -1;
	}
	if ((xc - xa) * (yb - ya) == (yc - ya) * (xb - xa))
	{
		printf("Одна прямая, а не треугольник");
		return -1;
	}
	v1 = triangle(&xa, &ya, &xb, &yb, &xc, &yc, &x0, &y0);
	v2 = triangle(&xb, &yb, &xc, &yc, &xa, &ya, &x0, &y0);
	v3 = triangle(&xc, &yc, &xa, &ya, &xb, &yb, &x0, &y0);
	if ((v1 == 0) && (v2 == 0) && (v3 == 0))
		printf("%d", 0);
	else if ((v1 == 1) || (v2 == 1) || (v3 == 1))
		printf("%d", 1);
	else
		printf("%d", 2);
	return 0;
}
