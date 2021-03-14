# Лабораторная работа 2, сортировки
# Калашков Павел ИУ7-26Б, "Гномья" сортировка. Версия 2
import tkinter as tk
import tkinter.messagebox as box
import time
import random


def sort(data, p):
    j = 1
    size = 0
    while size < len(data) and type(data[size]) == float:
        size += 1
    while j < size:
        if data[j - 1] <= data[j]:
            j += 1
        else:
            data[j - 1], data[j] = data[j], data[j - 1]
            if j > 1:
                j -= 1
    if p == 0:
        update(0)
    else:
        update(2)


def ent(var):
    if var == 0:
        try:
            arr[index[0]] = float(ent_entry.get())
            ent_entry.delete(0, last='end')
            if index[0] < 9:
                index[0] += 1
                ent_label.config(text='Введите а[{:d}]'.format(index[0]))
            else:
                ent_label.config(text='Массив введён.')
                ent_entry.config(state='readonly')
            update(0)
        except ValueError:
            if ent_entry.get() != '':
                box.showwarning(title='Warning!', message='Неправильный ввод!')
    elif var == 1:
        flag = 0
        for j in range(3):
            try:
                value = int(entry_arr_2[j].get())
                if value > 10000:
                    box.showwarning(title='Значение слишком велико', message='Значение слишком велико. Максимальная'
                                                                             ' длина 10 000. Введено значение '
                                                                             'по умолчанию')
                    length[j] = 500 * j + 500
                elif value >= 50:
                    length[j] = value
                elif value > 0:
                    box.showwarning(title='Значение слишком мало.', message='Значение слишком мало. Минимальная длина'
                                                                            ' равна 50. Введено значение по умолчанию.')
                    length[j] = 500 * j + 500
                else:
                    box.showwarning(title='Длина неверна', message='Длина - целое положительное число. Введены'
                                                                   ' значения по умолчанию.')
            except ValueError:
                if entry_arr_2[j].get() != '' and flag == 0:
                    box.showwarning('Неверный ввод.', message='Неверный ввод. Подайте, пожалуйста, нормальные числа'
                                                              ' на вход :) И да, введены значения по умолчанию.')
                    flag = 1
                elif entry_arr_2[j].get() == '' and flag == 0:
                    box.showwarning('Не все поля заполнены.', message='Не все поля заполнены. Введены '
                                                                      'значения по умолчанию.')
                    flag = 1
                length[j] = 500 * j + 500
        update(1)
    pass


def delete(var):
    if var == 0:
        ent_entry.config(state='normal')
        index[0] = 0
        ent_entry.delete(0, last='end')
        ent_label.config(text='Введите а[{:d}]'.format(index[0]))
        for j in range(10):
            arr[j] = '------------------'
        update(0)
    elif var == 1:
        for j in range(3):
            entry_arr_2[j].config(state='normal')
            entry_arr_2[j].delete(0, last='end')
        length[0] = 500
        length[1] = 1000
        length[2] = 1500
        for j in range(9):
            times[j] = '------------------'
        update(2)

    pass


def calculate():
    ent(1)
    for j in range(3):
        array1 = [0] * length[j]
        array1[0] = random.uniform(1, 2)
        for p in range(1, length[j]):
            array1[p] = array1[p-1] + random.uniform(1, 2)
        array2 = [0] * length[j]
        for p in range(length[j]):
            array2[p] = random.uniform(0, 10)
        array3 = [0] * length[j]
        array3[0] = random.uniform(10, 20)
        for p in range(1, length[j]):
            array3[p] = array3[p-1] - random.uniform(0, 2)
        start_time = time.time()
        sort(array1, 2)
        current_time = time.time()
        times[j*3] = analyse(current_time - start_time)
        start_time = time.time()
        sort(array2, 2)
        current_time = time.time()
        times[j * 3 + 1] = analyse(current_time - start_time)
        start_time = time.time()
        sort(array3, 2)
        current_time = time.time()
        times[j * 3 + 2] = analyse(current_time - start_time)
    update(2)


def analyse(var):
    if var > 0.01:
        return '{:2.5f}'.format(var) + ' c'
    elif var > 0.001:
        return '{:3.5f}'.format((var * 1e3)) + ' мс'
    elif var > 0.000001:
        return '{:3.3f}'.format((var * 1e6)) + ' мкс'
    else:
        return '{:3.3f}'.format((var * 1e10)) + ' нс'
    pass


def update(var):
    if var == 0:
        for j in range(10):
            entry_arr[j].config(state='normal')
            entry_arr[j].delete(0, last='end')
            entry_arr[j].insert(0, str(arr[j]))
            entry_arr[j].config(state='readonly')
    elif var == 1:
        for j in range(3):
            entry_arr_2[j].delete(0, last='end')
            entry_arr_2[j].insert(0, str(length[j]))
            entry_arr_2[j].config(state='readonly')
    elif var == 2:
        for j in range(9):
            table_arr[j].config(state='normal')
            table_arr[j].delete(0, last='end')
            table_arr[j].insert(0, times[j])
            table_arr[j].config(state='readonly')
    pass


def enter(event):
    ent(0)


arr = ['------------------'] * 10
index = [0]
length = [500, 1000, 1500]
times = ['------------------'] * 9
window = tk.Tk()
window.geometry("1500x500")
window.title("Лаб. 2 Сортировка")
main_label = tk.Label(
    master=window,
    font='Times 14',
    text='Сортировка массива a[] длиной до 10-ти элементов:'
)

main_label.grid(row=0, column=0, columnspan=10)

ent_label = tk.Label(
    master=window,
    font='Times 14',
    text='Введите a[0]:'
)
ent_label.grid(row=1, column=0)

ent_entry = tk.Entry(
    master=window,
    font='Times 14',
    width=10
)
ent_entry.bind("<Return>", enter)
ent_entry.grid(row=1, column=1)

del_button = tk.Button(
    master=window,
    font='Times 14',
    text='Очистить',
    command=lambda t=0: delete(t)
)
del_button.grid(row=2, column=0)

ent_button = tk.Button(
    master=window,
    font='Times 14',
    text='Ввод',
    command=lambda t=0: ent(t)
)
ent_button.grid(row=3, column=0)

sort_button = tk.Button(
    master=window,
    font='Times 14',
    text='Отсортировать',
    command=lambda t=arr, p=0: sort(t, p)
)
sort_button.grid(row=4, column=0)
arr_label1 = tk.Label(
    master=window,
    font='Times 14',
    text='a[i]'
)
arr_label1.grid(row=5, column=0)

arr_label2 = tk.Label(
    master=window,
    font='Times 14',
    text='i'
)
arr_label2.grid(row=6, column=0)

entry_arr = list()
for i in range(10):
    label = tk.Label(master=window, font='Times 14', text=str(i))
    label.grid(row=5, column=1+i)
    entry = tk.Entry(master=window, font='Times 14', width=12)
    entry.insert(0, '------------------')
    entry.config(state='readonly')
    entry_arr.append(entry)
    entry.grid(row=6, column=1+i)
part_two_label = tk.Label(master=window, font='Times 14', text='------------------------------------'
                                                               '-----------------------------------'
                                                               '------------------------------------'
                                                               '-----------------------------------'
                                                               '------------------------------------'
                                                               '-----------------------------------'
                                                               '------------------------------------')
part_two_label.grid(row=8, column=0, columnspan=20)
main_label_two = tk.Label(master=window, font='Times 14', text='Часть 2. Измерение времени "гномьей" сортировки на трёх'
                                                               ' массивах длин N1, N2, N3 (по умолчанию'
                                                               ' 500, 1000 и 1500'
                                                               ' соответственно. Минимальная длина 50'
                                                               ', максимальная 10 000.')
main_label_two.grid(row=9, column=0, columnspan=20)

entry_arr_2 = list()
for i in range(3):
    label = tk.Label(master=window, font='Times 14', text='Длина N{:d}:'.format(i+1))
    label.grid(row=10+i, column=0)
    entry = tk.Entry(master=window, font='Times 14', width=10)
    entry_arr_2.append(entry)
    entry.grid(row=10+i, column=1)
del_two_button = tk.Button(master=window, font='Times 14', text='Очистить', command=lambda t=1: delete(t))
del_two_button.grid(row=13, column=0)
ent_two_button = tk.Button(master=window, font='Times 14', text='Ввод', command=lambda t=1: ent(t))
ent_two_button.grid(row=14, column=0)
calculate_button = tk.Button(master=window, font='Times 14', text='Вычислить', command=calculate)
calculate_button.grid(row=15, column=0)
table_1_0 = tk.Entry(master=window, width=12, font='Times 14')
table_1_0.insert(0, 'Восходящий')
table_1_0.config(state='readonly')
table_1_0.grid(row=11, column=3)
table_2_0 = tk.Entry(master=window, width=12, font='Times 14')
table_2_0.insert(0, 'Случайный')
table_2_0.config(state='readonly')
table_2_0.grid(row=12, column=3)
table_3_0 = tk.Entry(master=window, width=12, font='Times 14')
table_3_0.insert(0, 'Нисходящий')
table_3_0.config(state='readonly')
table_3_0.grid(row=13, column=3)
table_0_1 = tk.Entry(master=window, width=12, font='Times 14')
table_0_1.insert(0, '        N1    ')
table_0_1.config(state='readonly')
table_0_1.grid(row=10, column=4)
table_0_2 = tk.Entry(master=window, width=12, font='Times 14')
table_0_2.insert(0, '        N2    ')
table_0_2.config(state='readonly')
table_0_2.grid(row=10, column=5)
table_0_3 = tk.Entry(master=window, width=12, font='Times 14')
table_0_3.insert(0, '        N3    ')
table_0_3.config(state='readonly')
table_0_3.grid(row=10, column=6)
table_arr = []
for i in range(9):
    entry = tk.Entry(master=window, width=12, font='Times 14')
    entry.insert(0, '------------------')
    entry.config(state='readonly')
    entry.grid(row=11+(i % 3), column=4 + (i // 3))
    table_arr.append(entry)
window.mainloop()
