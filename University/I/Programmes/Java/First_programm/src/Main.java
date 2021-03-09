// Программа нахождения параметров пятиугольной призмы по параметрам описанного цилиндра
// Автор: Калашков П.А. ИУ7-16Б

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Радиус и высота
        double r, h;
        // Площадь основания, объём, ребро основания, площадь боковой и полной поверхностей
        double s, v, t, sBok, sPol;
        System.out.print("Введите радиус цилиндра и высоту: ");
        r = scanner.nextDouble();
        h = scanner.nextDouble();
        if ((r > 0) && (h > 0)) { // проверка на положительность радиуса и высоты
            s = 2.5 * r * r * Math.sin(2 * Math.PI / 5); // вычисление площади основания
            v = s * h; // вычисление объёма
            t = r * Math.sqrt((5 - Math.sqrt(5)) / 2); // вычисление ребра основания
            sBok = 5 * t * h; // вычисление площади боковой поверхности
            sPol = (2 * s) + sBok; // вычисление площади полной поверхности
            // вывод результатов
            System.out.println("Параметры правильной пятиугольной призмы, вписанной в цилиндр с данными радиусом и высотой: ");
            System.out.printf("Объём: %3.5g \n", v);
            System.out.printf("Площадь боковой поверхности: %9.7g \n", sBok);
            System.out.printf("Площадь полной поверхности: %9.7g \n", sPol);
        } else System.out.println("Некорректный ввод :(");

    }
}
