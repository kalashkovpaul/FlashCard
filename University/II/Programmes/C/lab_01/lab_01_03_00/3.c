//Лаб. работа 1, Задача №3
//Автор: Калашков Павел ИУ7-26Б, Вариант 8 (вариант задачи 0)
#include <stdio.h>

int main(void)
{
	float h, t, m, mn, bmi;

	printf("Вычисление нормального веса человека и индекса массы его тела.\n");
	//ввод данных
	printf("Введите рост человека в сантиметрах: ");
	scanf("%f", &h);
	printf("Введите обхват грудной клетки в сантиметрах: ");
	scanf("%f", &t);
	printf("Введите масссут тела в килограммах: ");
	scanf("%f", &m);

	mn = (h * t) / 240;
	bmi = m / ((h / 100) * (h / 100));
	printf("Нормальный вес человека: %f\n", mn);
	printf("Индекс массы тела: %f\n", bmi);

	return 0;
}
	