import java.util.Scanner;

// Дополнительное задание по треугольнику
// Автор: Калашков П.А. ИУ7-16Б
public class Main {
    public static void main(String[] args) {
        double xa, ya, xb, yb, xc, yc; // координаты точек
        double ab, bc, ac; // длины сторон
        double p, s, h; // полупериметр, площадь, высота
        Scanner scanner = new Scanner(System.in);
        // ввод координат
        System.out.print("Введите координаты первой точки: ");
        xa = scanner.nextDouble();
        ya = scanner.nextDouble();
        System.out.print("Введите координаты второй точки: ");
        xb = scanner.nextDouble();
        yb = scanner.nextDouble();
        System.out.print("Введите координаты третьей точки: ");
        xc = scanner.nextDouble();
        yc = scanner.nextDouble();
        // определение длин сторон как длин векторов
        ab = Math.sqrt(((xb - xa)*(xb - xa) + (yb - ya)*(yb - ya)));
        bc = Math.sqrt(((xc - xb)*(xc - xb) + (yc - yb)*(yc - yb)));
        ac = Math.sqrt(((xc - xa)*(xc - xa) + (yc - ya)*(yc - ya)));
        // проверка на принадлежность одной прямой
        if ((ab + bc == ac) || (ab + ac == bc) || (bc + ac == ab)) {
            System.out.println("Не нужно вводить координаты прямой");
        } else {
            // определение площади по формуле Герона
            p = (ab + bc + ac) / 2;
            s = Math.sqrt(p * (p - ab) * (p - bc) * (p - ac));
            System.out.printf("Площадь %3.5g \n", s);
            // определение наименьшей стороны и высоты к ней
            if ((ab <= bc) && (ab <= ac)) {
                h = 2 * s / ab;
            } else if ((bc <= ab) && (bc <= ac)) {
                h = 2 * s / bc;
            } else h = 2 * s / ac;
            System.out.printf("Длина высоты, проведённой из наименьшего угла %3.5g \n", h);
        }
    }
}
