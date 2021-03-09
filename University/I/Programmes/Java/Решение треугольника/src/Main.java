// Решение треугольника
// Автор: Калашков П.А. ИУ7-16Б

import java.util.Scanner;
import  java.lang.Math;
public class Main {
    public static double length(int x1, int y1, int x2, int y2) {
        return Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)); // вычисление длины вектора
    }

    public static double degrees(double a, double b, double c) {
        return Math.toDegrees(Math.acos((b*b + c*c - a*a)/(2*b*c))); // вычисление угла по теореме косинусов
    }

    public static boolean isEqualLengths(double a, double b, double c) { // равнобедренный ли треугольник
        return (a == b) || (b == c) || (a == c);
    }

    public static boolean isOrt(double xa, double xb) {
        return (xa == xb); // ортогональна ли оси х
    }

    public static double kLine(double xa, double ya, double xb, double yb) {
        if (!isOrt(xa, xb)) {
            return (yb - ya) / (xb - xa); // коэффициент прямой
        } else return 0;
    }

    public static double bLine(double xa, double ya, double xb, double yb) {
        if(!isOrt(xa, xb)) {
            return ya - kLine(xa, ya, xb, yb) * xa; // свободный член прямой
        } else return 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int xa, ya; // координаты точки А
        int xb, yb; // координаты точки В
        int xc, yc; // координаты точки С
        int x, y; // координаты точки, введённой далее
        // ввод координат
        System.out.print("Введите координаты первой точки: ");
        xa = scanner.nextInt();
        ya = scanner.nextInt();
        System.out.print("Введите координаты второй точки: ");
        xb = scanner.nextInt();
        yb = scanner.nextInt();
        System.out.print("Введите коориднаты третьей точки: ");
        xc = scanner.nextInt();
        yc = scanner.nextInt();

        // вычисление длин сторон
        double a = length(xb, yb, xc, yc);
        double b = length(xa, ya, xc, yc);
        double c = length(xa, ya, xb, yb);

        // биссектриса
        double l = 0;

        // вычисление градусов
        double aDeg = degrees(a, b, c);
        double bDeg = degrees(b, a, c);
        double cDeg = degrees(c, a, b);

        // определение наибольшего угла и биссектрисы
        double maxAngle = 0;
        if (aDeg > maxAngle) {
            maxAngle = aDeg;
            l =  2 * b * c * Math.cos(Math.toRadians(maxAngle / 2)) / (b + c);
        }
        if (bDeg > maxAngle) {
            maxAngle = bDeg;
            l = 2 * a * c * Math.cos(Math.toRadians(maxAngle / 2)) / (a + c);
        }
        if (cDeg > maxAngle) {
            maxAngle = cDeg;
            l = 2 * a * b * Math.cos(Math.toRadians(maxAngle / 2)) / (a + b);
        }

        // переменные для коэффициентов прямых
        double kAb = 0, kBc = 0, kAc = 0;

        // переменные для свободных членов прямых
        double bAb = 0, bBc = 0, bAc = 0;

        // переменные для определения полуплоскостей
        int mAb = 0, mAc = 0, mBc = 0;

        // переменные для полуплоскостей
        double delta, deltaM;

        // переменные для расстояний
        double pAb, pBc, pAc, p = 0;

        // если три точки лежат на одной прямой
        if (a + b == c || a + c == b || b + c == a) {
            System.out.println("Точки лежат на одной прямой :(");
        } else {
            System.out.printf("Длины сторон треугольника равны: %g, %g, %g \n", a, b, c);
            System.out.printf("Углы треугольника равны %g, %g, %g \n", aDeg, bDeg, cDeg);
            System.out.printf("Наибольший угол равен %g \n", maxAngle);
            System.out.printf("Биссектриса наибольшего угла %g \n", l);

            if (isEqualLengths(a, b, c)) {
                System.out.println("Треугольник равнобедренный");
            } else {
                System.out.println("Треугольник не равнобедренный");
            }
            // определяем прямые
            if (!isOrt(xa, xb)) {
                kAb = kLine(xa, ya, xb, yb);
                bAb = bLine(xa, ya, xb, yb);
            }
            if (!isOrt(xb, xc)) {
                kBc = kLine(xb, yb, xc,yc);
                bBc = bLine(xb, yb, xc, yc);
            }
            if (!isOrt(xa, xc)) {
                kAc = kLine(xa, ya, xc, yc);
                bAc = bLine(xa, ya, xc, yc);
            }
            // ввод координат точки
            System.out.print("Введите координаты точки: ");
            x = scanner.nextInt();
            y = scanner.nextInt();
            // полуплоскость АВ
            // переменная mАb хранит 1, если заданная точка по одну сторону с точкой С
            //                       0, если заданная точка лежит на АВ
            //                      -1, если заданная точка лежит по разные стороны с точкой С
            if (isOrt(xa, xb)) {
                if (((x > 0) && (xc > 0)) || ((x < 0) && (xc < 0)))  mAb = 1;
            } else {
                delta = yc - kAb * xc - bAb;
                deltaM = y - kAb * x - bAb;
                if ((delta > 0) && (deltaM > 0) || (delta < 0) && (deltaM < 0)) mAb = 1;
                else if (deltaM == 0) mAb = 0;
                else mAb = -1;
            }
            // полуплоскость ВС
            // переменная mBc хранит 1, если заданная точка по одну сторону с точкой A
            //                       0, если заданная точка лежит на BC
            //                      -1, если заданная точка лежит по разные стороны с точкой A

            if (isOrt(xb, xc)) {
                if (((x > 0) && (xa > 0)) || ((x < 0) && (xa < 0)))  mBc = 1;
            } else {
                delta = ya - kBc * xa - bBc;
                deltaM = y - kBc * x - bBc;
                if ((delta > 0) && (deltaM > 0) || (delta < 0) && (deltaM < 0)) mBc = 1;
                else if (deltaM == 0) mBc = 0;
                else mBc = -1;
            }
            // полуплоскость AC
            // переменная mАc хранит 1, если заданная точка по одну сторону с точкой B
            //                       0, если заданная точка лежит на AC
            //                      -1, если заданная точка лежит по разные стороны с точкой B
            if (isOrt(xa, xc)) {
                if (((x > 0) && (xb > 0)) || ((x < 0) && (xb < 0)))  mAc = 1;
            } else {
                delta = yb - kAc * xb - bAc;
                deltaM = y - kAc * x - bAc;
                if ((delta > 0) && (deltaM > 0) || (delta < 0) && (deltaM < 0)) mAc = 1;
                else if (deltaM == 0) mAc = 0;
                else mAc = -1;
            }
            // непосредственно определение, лежит ли
            if ((mAb == mBc) && (mBc == mAc) && (mAc == 1) || (mAb == 0) || (mBc == 0) || (mAc == 0)) {
                System.out.println("Принадлежит");
                // теперь нахождение расстояний
                // до прямой АВ
                if (isOrt(xa, xb)) pAb = Math.abs(x);
                else pAb = Math.abs(kAb * x - y + bAb) / Math.sqrt(kAb*kAb + 1);
                // до прямой ВС
                if (isOrt(xb, xc)) pBc = Math.abs(x);
                else pBc = Math.abs(kBc * x - y + bBc) / Math.sqrt(kBc*kBc + 1);
                //
                if (isOrt(xa, xc)) pAc = Math.abs(x);
                else pAc = Math.abs(kAc * x - y + bAc) / Math.sqrt(kAc*kAc + 1);
                // определение ближайшей прямой
                if ((pAc <= pBc) && (pAc <= pAb)) p = pAc;
                if ((pAb <= pBc) && (pAb <= pAc)) p = pAb;
                if ((pBc <= pAb) && (pBc <= pAc)) p = pBc;
                System.out.printf("Расстояние до ближайшей прямой или её продолжения %g", p);
            } else System.out.println("Не принадлежит");
        }

    }
}
