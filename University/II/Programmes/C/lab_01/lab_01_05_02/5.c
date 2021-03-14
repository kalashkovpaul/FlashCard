// Лаб. работа 1, Задача №5
// Автор: Калашков Павел ИУ7-26Б, Вариант 8, номер варианта 2
#include <stdio.h>

int fib(int *x)
// функция для вычисления числа Фибоначчи
{
	int a = 0, b = 1;
	while (*x != 0)
	{
		a += b;
		b = a - b;
		*x -= 1;
	}
	return a;
}


int main(void)
{	
	int n, x, rc;
	printf("Вычисления числа Фибоначчи по его номеру n.\n");
	printf("Введите номер числа (целое, неотрицательное): ");

	rc = scanf("%d", &n);
	if ((rc == 1) && (n >= 0))
	{
		if (n < 48)
		{
			x = fib(&n);
			printf("Число Фибоначчи: %d", x);
		}
		else
		{
			printf("Переполнение, слишком большое число.");
			return -1;
		}
	}
	else 
	{
		printf("Некорректный ввод");
		return -1;
	}
	
	return 0;
}
