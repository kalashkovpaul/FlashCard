// Лаб. работа 1, Задача №2
// Автор: Калашков Павел ИУ7-26Б, Вариант 8 (задача варианта 0)
#include <stdio.h>
#include <math.h>

int main(void)
{	
	float a, b, h, s;
	printf("Программа, высчитывающая периметр равнобедренной трапеции\n");
	printf("Введите первое основание трапеции: ");
	scanf("%f", &a);
	printf("Введите второе основание трапеции: ");
	scanf("%f", &b);
	printf("Введите высоту трапеции: ");
	scanf("%f", &h);
	 
	s = a + b + 2 * sqrt(h * h + ((a - b) / 2) * ((a - b) / 2));
	printf("Периметр трапеции: %g", s);
	
	return 0;
}
