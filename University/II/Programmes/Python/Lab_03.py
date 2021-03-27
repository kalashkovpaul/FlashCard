# Лабораторная работа №3 "Методы уточнения корней"
# Автор: Калашков Павел ИУ7-26Б, Вариант по журналу 8
# Метод Брента (библиотечная реализация) scipy.optimize
# На графике отметить локальные экстремумы
import tkinter as tk
import tkinter.messagebox as box
from matplotlib import pyplot
import numpy as np
import math
from scipy import optimize as opt


def enter():  # функция для ввода
    try:
        clear()
        a = float(a_entry.get())
        roots.append(a)
        b = float(b_entry.get())
        roots.append(b)
        if a > b:
            raise Exception("Ошибка: a должно быть меньше b!")
        h = float(h_entry.get())
        roots.append(h)
        if h <= 0:
            raise Exception("Ошибка: h должно быть положительным")
        eps = float(eps_entry.get())
        if eps <= 0 or eps >= 1:
            raise Exception("Ошибка: eps должно входить в (0, 1)")
        n_max = int(N_max_entry.get())
        if n_max <= 0:
            raise Exception("Ошибка: N_max должно быть положительным")
        calculate(a, b, h, eps, n_max)
        for i in range(len(row)):
            row[i] = '0'
    except ValueError:
        box.showwarning("Ошибка ввода!", "Все значения должны быть числами!")
    except Exception as err:
        box.showwarning("Ошибка ввода!", str(err.args[0]))


def calculate(a, b, h, eps, n_max):  # функция для вычисления корней
    try:
        a_true = a
        b_true = a + h
        begin = a
        end = a + h
        flag = False  # был ли уже хотя бы один корень
        while end < b:
            if abs(f(begin)) < 1e-8:
                if flag:
                    add_row()
                row[0] = "{:^10g}".format(int(row[0]) + 1)
                row[1] = "{:4.4g}".format(a_true) + "; " + "{:^4.4g}".format(b_true)
                row[2] = "{:^10.4g}".format(begin)
                roots.append(begin)
                row[3] = "{:^10.4e}".format(f(begin))
                row[4] = '1'
                row[5] = '0'
                a_true = b_true
                begin = a_true
                b_true += h
                end = b_true
                flag = True
            elif abs(f(end)) < 1e-8:
                if flag:
                    add_row()
                row[0] = "{:^10g}".format(int(row[0]) + 1)
                row[1] = "{:4.4g}".format(a_true) + "; " + "{:^4.4g}".format(b_true)
                row[2] = "{:^10.4g}".format(end)
                roots.append(end)
                row[3] = "{:^10.4e}".format(f(end))
                row[4] = '1'
                row[5] = '0'
                a_true = b_true + h
                begin = a_true
                b_true += 2 * h
                end = b_true
                flag = True
            elif f(begin) * f(end) < 0:
                if flag:
                    add_row()
                res = check(begin, end, eps, n_max)
                row[0] = "{:^10g}".format(int(row[0]) + 1)
                row[1] = "{:4.4g}".format(a_true) + "; " + "{:^4.4g}".format(b_true)
                row[2] = "{:^10.4g}".format(res[0])
                roots.append(res[0])
                row[3] = "{:^10.4e}".format(f(res[0]))
                row[4] = str(res[1].iterations)
                row[5] = str(int(not res[1].converged * 1))
                a_true = b_true
                begin = a_true
                b_true += h
                end = b_true
                flag = True
            else:
                begin = end
                b_true += h
                end = b_true
        b_true = b
        end = b_true
        if abs(f(begin)) < 1e-8:
            if flag:
                add_row()
            row[0] = "{:^10g}".format(int(row[0]) + 1)
            row[1] = "{:4.4g}".format(a_true) + "; " + "{:^4.4g}".format(b_true)
            row[2] = "{:^10.4g}".format(begin)
            roots.append(begin)
            row[3] = "{:^10.4e}".format(f(begin))
            row[4] = '1'
            row[5] = '0'
            a_true = b_true
            begin = a_true
            b_true += h
            end = b_true
            add_row()
        elif abs(f(end)) < 1e-8:
            if flag:
                add_row()
            row[0] = "{:^10g}".format(int(row[0]) + 1)
            row[1] = "{:4.4g}".format(a_true) + "; " + "{:^4.4g}".format(b_true)
            row[2] = "{:^10.4g}".format(end)
            roots.append(end)
            row[3] = "{:^10.4e}".format(f(end))
            row[4] = '1'
            row[5] = '0'
            a_true = b_true + h
            begin = a_true
            b_true += 2 * h
            end = b_true
            flag = True
        elif f(begin) * f(end) < 0:
            if flag:
                add_row()
            res = check(begin, end, eps, n_max)
            row[0] = "{:^10g}".format(int(row[0]) + 1)
            row[1] = "{:4.4g}".format(a_true) + "; " + "{:^4.4g}".format(b_true)
            row[2] = "{:^10.4g}".format(res[0])
            roots.append(res[0])
            row[3] = "{:^10.4e}".format(f(res[0]))
            row[4] = "{:^10.4g}".format(res[1].iterations)
            row[5] = str(not res[1].converged * 1)
            a_true = b_true
            begin = a_true
            b_true += h
            end = b_true
            add_row()
        else:
            if flag:
                row[1] = row[1][:row[1].find(';')] + "; " + str(b_true)
                add_row()
            else:
                row[0] = "{:^10g}".format(int(row[0]) + 1)
                row[1] = "{:4.4g}".format(a_true) + "; " + "{:^4.4g}".format(b_true)
                row[2] = "Корней нет"
                row[3] = "И значений тоже нет"
                row[4] = "Количества итераций нет"
                row[5] = "2"
                add_row()
        window.geometry(str(size[0]) + "x" + str(size[1]))
        build()
    except ValueError:
        raise Exception("Проверьте, чтобы функция существовала на всей области определения данной функции")


def check(a, b, eps, n_max):  # функция уточнения корней - через библиотечную функцию методом Брента
    try:
        res = opt.brentq(f, a=a, b=b, rtol=eps, maxiter=n_max, full_output=True)
        print(res)
    except ValueError:
        res = ('?', False, '?', '?', '1')
    except RuntimeError:
        print('Ряд не сходится за введённое количество итераций!')
        res = ('?', False, '?', '?', '?')

    return res


def add_row():  # функция для добавления ряда в таблицу с корнями
    element = []
    for i in range(6):
        column = tk.Entry(master=window, font='Times 14')
        column.insert(0, row[i])
        column.config(state='readonly')
        element.append(column)
        element[i].grid(row=coordinates[0], column=coordinates[1] + i)
    table.append(element)
    coordinates[0] += 1
    size[1] += 15


def clear():  # функция для очистки всего
    coordinates[0] = 4
    size[1] = 250
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j].grid_forget()
    table.clear()
    roots.clear()
    for i in range(len(row)):
        row[i] = '0'


def f(x):  # сама функция f(x)
    return x**2 - 4#math.sin(x)


def event_enter(event):  # для ввода через enter
    enter()


def build():
    x_range = np.linspace(roots[0], roots[1], 1000)
    y_range = np.sin(x_range)
    x_markers = roots[3:]
    for i in range(1, len(x_range) - 1):
        if (f(x_range[i - 1]) < f(x_range[i]) and f(x_range[i + 1]) < f(x_range[i])) or (f(x_range[i - 1]) > f(x_range[i]) and f(x_range[i + 1]) > f(x_range[i])):
            x_markers.append(x_range[i])
    x_range.sort()
    y_markers = np.sin(x_markers)
    pyplot.plot(x_range, y_range, '-g')
    pyplot.plot(x_markers, y_markers, 'rD')
    pyplot.show()


row = ['0'] * 6  # элементы для одного ряда
roots = []
table = []  # для таблицы
size = [1500, 250]  # для размера окна
coordinates = [4, 2]  # для координаты ряда
window = tk.Tk()  # главное окно
window.geometry("1500x250")
window.title("Лаб. 3 Уточнение корней")
# элементы интерфейса, 7 надписей, 5 полей ввода, 1 кнопка и заголовок таблицы для корней
main_label = tk.Label(
    master=window,
    font='Times 14',
    text='Таблица для функции f = sin(x):'
)
main_label.grid(row=0, column=0, columnspan=10)

data_label = tk.Label(
    master=window,
    font='Times 14',
    text='Входные даные: a - начало отрезка, b - конец отрезка (a < b), h - шаг разбиений (h > 0),'
         ' eps - точность (0 < eps < 1), Nmax - максимальное число итераций (Nmax > 0)'
)
data_label.grid(row=1, column=0, columnspan=10)
get_a = tk.Label(
    master=window,
    font='Times 14',
    text='Введите а:'
)
get_a.grid(row=2, column=0)

a_entry = tk.Entry(
    master=window,
    font='Times 14'
)
a_entry.bind("<Return>", event_enter)
a_entry.grid(row=2, column=1)

get_b = tk.Label(
    master=window,
    font='Times 14',
    text='Введите b:'
)
get_b.grid(row=3, column=0)

b_entry = tk.Entry(
    master=window,
    font='Times 14'
)
b_entry.bind("<Return>", event_enter)
b_entry.grid(row=3, column=1)

get_h = tk.Label(
    master=window,
    font='Times 14',
    text='Введите h:'
)
get_h.grid(row=4, column=0)

h_entry = tk.Entry(
    master=window,
    font='Times 14'
)
h_entry.bind("<Return>", event_enter)
h_entry.grid(row=4, column=1)

get_eps = tk.Label(
    master=window,
    font='Times 14',
    text='Введите eps:'
)
get_eps.grid(row=5, column=0)

eps_entry = tk.Entry(
    master=window,
    font='Times 14'
)
eps_entry.bind("<Return>", event_enter)
eps_entry.grid(row=5, column=1)

get_N_max = tk.Label(
    master=window,
    font='Times 14',
    text='Введите Nmax:'
)
get_N_max.grid(row=6, column=0)

N_max_entry = tk.Entry(
    master=window,
    font='Times 14'
)
N_max_entry.bind("<Return>", event_enter)
N_max_entry.grid(row=6, column=1)

ent = tk.Button(master=window, font='Times 10', text='Рассчёт', command=enter)
ent.grid(row=7, column=0)

# с третьего ряда начинаем таблицу, начиная с заголовка таблицы
head_0_0 = tk.Entry(master=window, font='Times 14')
head_0_0.insert(0, '        Номер корня')
head_0_0.config(state='readonly')
head_0_0.grid(row=3, column=2)

head_0_1 = tk.Entry(master=window, font='Times 14')
head_0_1.insert(0, '          [xi; x(i+1)]')
head_0_1.config(state='readonly')
head_0_1.grid(row=3, column=3)

head_0_2 = tk.Entry(master=window, font='Times 14')
head_0_2.insert(0, '                 x   ')
head_0_2.config(state='readonly')
head_0_2.grid(row=3, column=4)

head_0_3 = tk.Entry(master=window, font='Times 14')
head_0_3.insert(0, '                 f(x)   ')
head_0_3.config(state='readonly')
head_0_3.grid(row=3, column=5)

head_0_4 = tk.Entry(master=window, font='Times 14')
head_0_4.insert(0, '                  N   ')
head_0_4.config(state='readonly')
head_0_4.grid(row=3, column=6)

head_0_5 = tk.Entry(master=window, font='Times 14')
head_0_5.insert(0, '             Code  ')
head_0_5.config(state='readonly')
head_0_5.grid(row=3, column=7)

# вторая часть программы, построение графиа


window.mainloop()
