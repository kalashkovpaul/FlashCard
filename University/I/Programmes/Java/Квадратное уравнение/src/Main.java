//Решение квадратного уравнения
//Автор: Калашков П.А. ИУ7-16Б
import java.util.Scanner;
import static java.lang.Math.abs;
import static java.lang.Math.sqrt;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите коэффициенты квадратного уравнения: ");
        double a, b, c; // коэффициенты
        double D; // дискриминант
        double x; // икс, если он единственный
        double x1, x2; // иксы, если их два
        a = scanner.nextFloat();
        b = scanner.nextFloat();
        c = scanner.nextFloat();
        if (a == 0) {
            if (b == 0) {
                if (c == 0) {
                    System.out.println("x - любой"); //если верное тождество
                } else {
                    System.out.println("Решений нет"); //если неверное тождество
                }
            } else {
                x = -c/b;
                System.out.printf("x = %.5f", x); // если уравнение первой степени
            }
        } else { // уравнение второй степени
            D = b*b - 4*a*c; //дискриминант
            if (D > 0) {
                // если два корня. Если они большие - вывод в экспоненциальной форме
                x1 = (-b - sqrt(D))/(2*a);
                x2 = (-b + sqrt(D))/(2*a);
                System.out.printf("x1 = %.5g", x1);
                System.out.printf("x2 = %.5g", x2);
            } else if (D == 0) {
                x = -b/2*a; // если один корень. Если он большой - вывод в экспоненциальной форме
                System.out.printf("x = %.5g", x);
            } else {
                // если корней нет
                System.out.println("Решений нет");
            }
        }

    }
}
