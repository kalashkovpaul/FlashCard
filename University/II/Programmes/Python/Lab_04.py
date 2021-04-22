# Лабораторная работа №4, Калашков Павел ИУ7-26Б
# На плоскости заданы множество точек А и множество прямых В. Найти две
# такие различные точки из А, что проходящая через них прямая
# параллельна наибольшему количеству прямых из В.
# Дать графическое изображение результатов.

import tkinter as tk
import tkinter.messagebox as box


class Dot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line(object):
    def __init__(self, dot_1, dot_2):
        self.dot_1 = dot_1
        self.dot_2 = dot_2
        self.center = Dot((dot_1.x + dot_2.x) / 2, (dot_1.y + dot_2.y) / 2)
        self.A = dot_1.y - dot_2.y
        self.B = dot_2.x - dot_1.x
        self.C = dot_1.x * dot_2.y - dot_2.x * dot_1.y
        self.border_1 = dot_1
        self.border_2 = dot_2

    def print_info(self):
        print(str(self.A) + "x + " + str(self.B) + "y + " + str(self.C))

    def find_borders(self):
        if self.A == 0:
            self.border_1 = Dot((-size[0] - 50) * scale[1], self.dot_1.y)
            self.border_2 = Dot((size[0] + 50) * scale[1], self.dot_1.y)
        elif self.B == 0:
            self.border_1 = Dot(self.dot_1.x, (size[1] + 50) * scale[1])
            self.border_2 = Dot(self.dot_1.x, (-size[1] - 50) * scale[1])
        else:
            self.border_1 = Dot((-size[0] - 50) * scale[1], (-self.C - self.A * (-size[0] - 50) * scale[1]) / self.B)
            self.border_2 = Dot((size[0] + 50) * scale[1], (-self.C - self.A * (size[0] + 50) * scale[1]) / self.B)

    def print_line(self):
        self.find_borders()
        x1 = int(self.border_1.x / scale[1]) + size[0] / 2
        y1 = (-1) * int(self.border_1.y / scale[1]) + size[1] / 2
        x2 = int(self.border_2.x / scale[1]) + size[0] / 2
        y2 = (-1) * int(self.border_2.y / scale[1]) + size[1] / 2
        canvas.create_line(x1, y1, x2, y2, fill='green', activewidth=3)

    def print_target(self):
        self.find_borders()
        x1 = int(self.border_1.x / scale[1]) + size[0] / 2
        y1 = (-1) * int(self.border_1.y / scale[1]) + size[1] / 2
        x2 = int(self.border_2.x / scale[1]) + size[0] / 2
        y2 = (-1) * int(self.border_2.y / scale[1]) + size[1] / 2
        canvas.create_line(x1, y1, x2, y2, fill='red', activewidth=3)


def enter_dot():
    try:
        x, y = map(float, dots_entry.get().split())
        new_dot = Dot(x, y)
        is_new = True
        for dot in dots:
            if dot.x == new_dot.x and dot.y == new_dot.y:
                is_new = False
        if is_new:
            dots.append(new_dot)
            dot_string = "{:d}) ({:6.4f}; {:6.4f})".format(len(dots), x, y)
            dots_listbox.insert(len(dots), dot_string)
        else:
            box.showwarning("Такая точка уже есть в списке", "Такая точка уже есть. Введите другую точку.")
        dots_entry.delete(0, last='end')
    except ValueError:
        dots_entry.delete(0, last='end')
        box.showwarning("Ошибка ввода", "Вы ввели неверные координаты точки. Координаты точек\
         - вещественные числа, введённые через пробел")


def enter_dot_event(event):
    enter_dot()


def del_dots():
    dots.clear()
    dots_entry.delete(0, last='end')
    dots_listbox.delete(0, dots_listbox.size())


def enter_line():
    try:
        x1, y1 = map(float, line_dot_1_entry.get().split())
        x2, y2 = map(float, line_dot_2_entry.get().split())
        if x1 == x2 and y1 == y2:
            raise ValueError
        first_dot = Dot(x1, y1)
        second_dot = Dot(x2, y2)
        new_line = Line(first_dot, second_dot)
        is_new = True
        for line in lines:
            if line.A == new_line.A and line.B == new_line.B and line.C == new_line.C:
                is_new = False
        if is_new:
            lines.append(new_line)
            first_dot_string = "{:d}) ({:6.4f}; {:6.4f})".format(len(lines), x1, y1)
            second_dot_string = "{:d}) ({:6.4f}; {:6.4f})".format(len(lines), x2, y2)
            lines_listbox_1.insert(len(lines), first_dot_string)
            lines_listbox_2.insert(len(lines), second_dot_string)
        else:
            box.showwarning("Такая прямая уже есть в списке", "Такая прямая уже есть. Введите другие две точки.")
        line_dot_1_entry.delete(0, last='end')
        line_dot_2_entry.delete(0, last='end')
    except ValueError:
        line_dot_1_entry.delete(0, last='end')
        line_dot_2_entry.delete(0, last='end')
        box.showwarning("Ошибка ввода", "Вы ввели неверные координаты точек. Координаты точки\
                 - вещественные числа, введённые через пробел. Точки должны быть различными.")


def enter_line_event(event):
    enter_line()


def del_lines():
    line_dot_1_entry.delete(0, last='end')
    line_dot_2_entry.delete(0, last='end')
    lines.clear()
    lines_listbox_1.delete(0, lines_listbox_1.size())
    lines_listbox_2.delete(0, lines_listbox_2.size())


def is_parallel(line_1, line_2):
    if line_1.A == 0 and line_2.A == 0 or line_1.B == 0 and line_2.B == 0:
        return 1
    if line_1.A != 0 and line_1.B != 0 and line_2.A != 0 and line_2.B != 0 \
            and abs(line_1.A / line_2.A - line_1.B / line_2.B) < 1e-8:
        return 1
    return 0


def find():
    maximum = 0
    counter = 0
    target_line = None
    for dot_1 in dots:
        for dot_2 in dots:
            if dot_1 != dot_2:
                line_1 = Line(dot_1, dot_2)
                for line_2 in lines:
                    if is_parallel(line_1, line_2):
                        counter += 1
                    if counter > maximum:
                        maximum = counter
                        target_line = line_1
    return target_line


def is_inside(dot):
    if 0 < dot.x / scale[1] + size[0]/2 < size[0] and 0 < dot.y / scale[1] - size[1]/2 < size[1]:
        return True
    else:
        return False


def find_scale():
    min_x = 100000000000
    min_y = 100000000000
    max_x = -100000000000
    max_y = -100000000000
    for dot in dots:
        if dot.x > max_x:
            max_x = dot.x
        if dot.x < min_x:
            min_x = dot.x
        if dot.y > max_y:
            max_y = dot.y
        if dot.y < min_y:
            min_y = dot.y
    for line in lines:
        dot = line.dot_1
        if dot.x > max_x:
            max_x = dot.x
        if dot.x < min_x:
            min_x = dot.x
        if dot.y > max_y:
            max_y = dot.y
        if dot.y < min_y:
            min_y = dot.y
        dot = line.dot_2
        if dot.x > max_x:
            max_x = dot.x
        if dot.x < min_x:
            min_x = dot.x
        if dot.y > max_y:
            max_y = dot.y
        if dot.y < min_y:
            min_y = dot.y
    scale[1] = max(abs(max_x - min_x) / size[0] * 2, abs(max_y - min_y) / size[1] * 2) * 1.1


def build():
    canvas.delete("all")
    find_scale()
    for line in lines:
        line.print_line()


def find_and_build():
    if len(dots) == 0 or len(lines) == 0:
        box.showwarning("Недостаточное количество элементов", "Элементов недостаточно. Введите больше элементов")
    build()
    target = find()
    if target is not None:
        target.print_target()


dots = []  # массив для точек
lines = []  # координаты точек, задающих прямую
scale = [1, 1]  # масштаб для canvas
size = [1600, 600]
main_window = tk.Tk()
main_window.geometry("1600x1500")
main_window.title("Решение планиметрических задач")
dots_listbox = tk.Listbox(master=main_window, font='Times 14', height=5)
lines_listbox_1 = tk.Listbox(master=main_window, font='Times 14', height=5)
lines_listbox_2 = tk.Listbox(master=main_window, font='Times 14', height=5)

task_label = tk.Label(master=main_window, text='На плоскости заданы множество точек А и множество прямых В. Найти две \
такие различные точки из А, что проходящая через них прямая \
параллельна наибольшему количеству прямых из В. ',
                      font='Times 14')
task_label.grid(row=0, column=0, columnspan=100)

dots_label = tk.Label(master=main_window, text='Задать точку из множества А, ввести координаты по х, у через \
пробел:', font='Times 14')
dots_label.grid(row=1, column=0)
dots_entry = tk.Entry(master=main_window, font='Times 14')
dots_entry.bind("<Return>", enter_dot_event)
dots_entry.grid(row=1, column=1)
dots_button = tk.Button(master=main_window, text='Добавить точку', font='Times 14', command=enter_dot)
dots_button.grid(row=1, column=2)
dots_listbox_label = tk.Label(master=main_window, text='Введённые точки:', font='Times 14')
dots_listbox_label.grid(row=1, column=3)
dots_listbox.grid(row=1, column=4, rowspan=2)
dots_del_button = tk.Button(master=main_window, text='Сброс', font='Times 14', command=del_dots)
dots_del_button.grid(row=2, column=2)

lines_label = tk.Label(master=main_window, text='Задать прямую из множества В, вести координаты двух точек', font='\
Times 14')
lines_label.grid(row=3, column=0)
line_dot_1_label = tk.Label(master=main_window, text='Задать первую точку, ввести координаты по х, у через \
пробел:', font='Times 14')
line_dot_1_label.grid(row=4, column=0)
line_dot_1_entry = tk.Entry(master=main_window, font='Times 14')
line_dot_1_entry.bind("<Return>", enter_line_event)
line_dot_1_entry.grid(row=4, column=1)
line_dot_2_label = tk.Label(master=main_window, text='Задать вторую точку, ввести координаты по х, у через \
пробел:', font='Times 14')
line_dot_2_label.grid(row=5, column=0)
line_dot_2_entry = tk.Entry(master=main_window, font='Times 14')
line_dot_2_entry.bind("<Return>", enter_line_event)
line_dot_2_entry.grid(row=5, column=1)
lines_button = tk.Button(master=main_window, text='Добавить прямую', font='Times 14', command=enter_line)
lines_button.grid(row=6, column=0)
lines_del_button = tk.Button(master=main_window, text='Сброс', font='Times 14', command=del_lines)
lines_del_button.grid(row=7, column=0)
lines_listbox_label = tk.Label(master=main_window, text='Точки, задающие введённые прямые:')
lines_listbox_1.grid(row=4, column=2, rowspan=3)
lines_listbox_2.grid(row=4, column=3, rowspan=3)

final_button = tk.Button(master=main_window, text='Найти точки, построить иллюстрацию', font='Arial\
 16', command=find_and_build)
final_button.grid(row=8, column=0)

canvas = tk.Canvas(height=size[1], width=size[0], bg='white')
canvas.grid(row=9, column=0, columnspan=7)
main_window.mainloop()
