// Лаб. работа 1, задача 8
// Автор: Калашков Павел ИУ7-16Б, Вариант 8, вариант задачи 0

#include <stdio.h>

int binary(unsigned *b, unsigned x)
// переводит десятичное число x в двоичное b, возращает длину числа b
{
	int p = 0, a = 1, c = 1;
	while (x > 0)
	{
		p = x % 2;
		x /= 2;
		*b += p * c;
		c *= 10;
		a++;
	}
	return a;
}


void second_shift(unsigned *x, int n)
{
	*x = (((*x) >> n) | ((*x) << (32 - n)));
}


int main(void)
{
	int i, n, ina, inn;
	unsigned a, b = 0;
	printf("Циклический двиг беззнакового целового числа длиной 4 байта на n позиций. \n");
	printf("Введите число: ");
	ina = scanf("%u", &a);
	printf("Введите число n: ");
	inn = scanf("%d", &n);
	if ((ina == 1) && (inn == 1) && (n >= 0))
	{
		second_shift(&a, n);
		binary(&b, a);
		printf("%u\n", b);
		printf("Result: ");
		for (i = 0; i < 32; i++)
		{
			printf("%c", (a & (1 << (31 - i))) ? '1' : '0');
		}
	} 
	else 
	{
		printf("Error: ");
		return -1;
	}	
	return 0;
}

