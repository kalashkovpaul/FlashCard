
// Бабочка по функциям
// Автор: Калашков П.А. ИУ7-16Б

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        boolean flag = false; // флажок, принадлежит ли точка
        int a = 1; // запускать ли ещё раз
        double x, y; //
        Scanner scanner = new Scanner(System.in);
        while (a == 1) {
            System.out.print("Введите координаты точки: ");
            x = scanner.nextDouble();
            y = scanner.nextDouble();
            if ((x >= -9) && (x <= -1)) { // левые крылья
                // левое верхнее крыло
                if ((y <= (-1 / 8) * (x+9)*(x+9) + 8) && (((x <= -8) && (y >= 7*(x+8)*(x+8) + 1)) || ((x >= -8) && (x <= -1) && y >= 1/49 * (x+1)*(x+1)))) {
                    System.out.println("Принадлежит, левое верхнее крыло");
                    flag = true;
                } else if (((x >= -8) && (x <= -2) && (y >=  (-1/3) * (x+5)*(x+5) - 7) && (y <= (-4/49) * (x+1)*(x+1))) || ((x >= -2) && (x <= -1) && (y >= (-2)* (x+1)* (x+1) - 2) && (y <= (-4/49) * (x+1)*(x+1)))) {
                    // левое нижнее крыло
                    System.out.println("Принадлежит, левое нижнее крыло");
                    flag = true;
                }
            }
            if ((x >= 1) && (x <= 9)) { // правые крылья
                // правое верхнее крыло
                if (((x >= 1) && (x <= 8) && (y >= (-1/49) * (x-1)*(x-1)) && (y <= (-1/8) * (x-9)*(x-9) + 8)) || ((x >=8) && (x <= 9) && (y >= 7 * (x-8)*(x-8) + 1) && (y <= (-1/8) * (x-9)*(x-9) + 8))) {
                    System.out.println("Принадлежит, правое верхнее крыло");
                    flag = true;
                } else if (((x >= 1) && (x <= 2) && (y >= (-2)*(x-1)*(x-1) - 2) && (y <= (-4/49) * (x-1)*(x-1))) || ((x >= 2) && (x <= 9) && (y >=  (-1/3) * (x-5)*(x-5) - 7) && (y <= (-4/49) * (x-1)*(x-1)))) {
                    // правое нижнее крыло
                    System.out.println("Принадлежит, правое нижнее крыло");
                    flag = true;
                }
            }
            if ((x >= -1) && (x <= 1)) { // пузико
                if ((y >= 4*x*x - 6) && (y <= -4*x*x +2)) {
                    System.out.println("Принадлежит, пузико");
                    flag = true;
                }
            }
            if ((x >= -2) && (x <= 0) && (y == -1.5*x + 2)) {
                // левый усик
                System.out.println("Принадлежит, левый усик");
                flag = true;
            }
            if ((x >= 0) && (x <= 2) && (y == 1.5*x +2)) {
                // правый усик
                System.out.println("Принадлежит, правый усик");
                flag = true;
            }
            if (!flag) System.out.println("Не принадлежит");
            flag = false;
            System.out.println("Ещё разок?) Введите 1 или 0");
            a = scanner.nextInt();
            if (a == 0) {
                System.out.println("Спасибо, что пользовались программой :)");
                break;
            }
        }
    }
}
