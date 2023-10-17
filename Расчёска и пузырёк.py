import numpy as np
from numba import njit, jit
import random
import matplotlib.pyplot as plt


class KnuthStep:
    def __init__(self, N):
        self.N = N
        self.t = int(np.log2(self.N) - 1)
        self.i = 0
        self.h = np.ones(self.t, dtype=int)
        for j in range(self.t - 1, 0, -1):
            self.h[j - 1] = 3 * self.h[j] + 1

    def next_step(self):
        if self.i >= self.t - 1:
            return 1

        step = self.h[self.i]
        self.i += 1
        return step


class BiStep:
    def __init__(self, N):
        self.N = N
        self.step = self.N

    def next_step(self):
        if self.step == 1:
            return 1
        self.step = self.step // 2
        return self.step


class BubleStep:
    def __init__(self, N):
        self.N = N

    def next_step(self):
        return 1


def comb_sort(sequince, class_sort):
    step_generator = class_sort(len(sequince))
    step = step_generator.next_step()
    global_swap = 0
    global_compare = 0
    while True:
        swap = 0
        i = 0

        while i + step < len(sequince):
            global_compare += 1
            if sequince[i] > sequince[i + step]:
                sequince[i], sequince[i + step] = sequince[i + step], sequince[i]
                swap += 1
            i = i + 1
            global_swap += swap
        if step == 1 and swap == 0:
            break

        step = step_generator.next_step()

    return global_swap, global_compare


def brush(sequince):
    global_swap = 0
    global_compare = 0
    n = len(sequince)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            j = i - gap
            while j >= 0 and sequince[j] > sequince[j + gap]:
                sequince[j], sequince[j + gap] = sequince[j + gap], sequince[j]
                global_swap += 1
                global_compare += 1
                j -= gap
            else:
                global_compare += 1
        gap = gap // 2

    return global_swap, global_compare


def ordinary_bubble(sequince):
    global_swap = 0
    global_compare = 0
    n = len(sequince)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sequince[j] > sequince[j + 1]:
                sequince[j], sequince[j + 1] = sequince[j + 1], sequince[j]
                global_swap += 1
                global_compare += 1
            else:
                global_compare += 1
    return global_swap, global_compare


def graf1():
    Bi = []
    Buble = []
    Knut = []

    scope = 10 ** 3
    Size = [i for i in range(3, scope, 20)]
    for n in Size:
        a = np.random.randint(-n, n, n)
        b = a.copy()
        c = a.copy()
        Bi.append(comb_sort(a, BiStep))
        Buble.append(comb_sort(b, BubleStep))

    mosaic = '''
    SC
    '''
    fig, ax = plt.subplot_mosaic(mosaic=mosaic)
    # fig, ax = plt.subplots(2, 1, layout='constrained')
    fig.suptitle('Зависимость сложности вычисления сортировки в зависимости от размера массива')

    ax['S'].plot(Size, [time[0] for time in Buble], Size, [time[0] for time in Bi], Size, [time[0] for time in Knut])
    ax['S'].set_ylabel('Число операций обмена')
    ax['S'].set_xlabel('Размер массива')
    ax['S'].grid()
    ax['S'].legend(['Сортировка пузырьком', 'Сортировка расчёской', 'Сортировка Шелла с шагом Кнутта'])

    ax['C'].plot(Size, [time[1] for time in Buble], Size, [time[1] for time in Bi], Size, [time[1] for time in Knut])
    ax['C'].set_ylabel('Число операций сравнений')
    ax['C'].set_xlabel('Размер массива')
    ax['C'].grid()
    ax['C'].legend(['Сортировка пузырьком', 'Сортировка расчёской', 'Сортировка Шелла с шагом Кнутта'])
    plt.show()


def degree_of_sorting(n):
    degree = []
    sequince = np.arange(n)
    np.random.shuffle(sequince)
    sequince1 = sequince.copy()
    sequince2 = sequince.copy()
    left = []
    right = []

    step = 1
    while True:
        left.append(sequince1.copy())
        swap = 0
        i = 0
        while i + step < len(sequince1):
            if sequince1[i] < sequince1[i + step]:
                sequince1[i], sequince1[i + step] = sequince1[i + step], sequince1[i]
                swap += 1
            i = i + 1
        if step == 1 and swap == 0:
            break
    while True:
        right.append(sequince2.copy())
        swap = 0
        i = 0
        while i + step < len(sequince2):
            if sequince2[i] > sequince2[i + step]:
                sequince2[i], sequince2[i + step] = sequince2[i + step], sequince2[i]
                swap += 1
            i = i + 1
        if step == 1 and swap == 0:
            break

    for i in left[::-1]:
        degree.append(i)
    degree.append(sequince)
    for i in right:
        degree.append(i)
    degree = np.array(degree)
    return degree, len(left)


def graf2(n=100):
    degree = degree_of_sorting(n)
    Bi = []
    Buble = []
    Knut = []
    for seq in degree[0]:
        a = seq.copy()
        b = seq.copy()
        c = seq.copy()
        Bi.append(comb_sort(a, BiStep))
        Buble.append(comb_sort(b, BubleStep))
        Knut.append((comb_sort(c, KnuthStep)))

    mosaic = '''
    SC
    '''
    fig, ax = plt.subplot_mosaic(mosaic=mosaic)
    # fig, ax = plt.subplots(2, 1, layout='constrained')
    fig.suptitle('Зависимость сложности вычисления сортировки в зависимости степени отсортированности массива')

    ox = range(len(degree[0]))

    ax['S'].plot(ox, [time[0] for time in Buble], ox, [time[0] for time in Bi], ox, [time[0] for time in Knut])
    ax['S'].set_ylabel('Число операций обмена')
    ax['S'].set_xlabel('Степень отсортированности')
    ax['S'].grid()
    ax['S'].legend(['Сортировка пузырьком', 'Сортировка расчёской', 'Сортировка Шелла с шагом Кнутта'],
                   loc='upper right')
    ax['S'].vlines(degree[1], 0, 4.1 * 10 ** 7, colors='r')

    ax['C'].plot(ox, [time[1] for time in Buble], ox, [time[1] for time in Bi], ox, [time[1] for time in Knut])
    ax['C'].set_ylabel('Число операций сравнений')
    ax['C'].set_xlabel('Степень отсортированности')
    ax['C'].grid()
    # ax['C'].legend(['Сортировка пузырьком', 'Сортировка расчёской', 'Сортировка Шелла с шагом Кнутта'], loc='upper right')
    ax['C'].vlines(degree[1], 0, 260_000, colors='r')
    plt.show()


def new_graf1():
    Shell = []
    Buble = []
    Knuth = []

    scope = 10 ** 3
    Size = [i for i in range(3, scope, 20)]
    for n in Size:
        a = np.random.randint(-n, n, n)
        b = a.copy()
        c = a.copy()
        Shell.append(brush(a))
        Buble.append(ordinary_bubble(b))
        Knuth.append(comb_sort(c, KnuthStep))


    mosaic = '''
    SC
    '''
    fig, ax = plt.subplot_mosaic(mosaic=mosaic)
    # fig, ax = plt.subplots(2, 1, layout='constrained')
    fig.suptitle('Зависимость сложности вычисления сортировки в зависимости от размера массива')

    bubble_swap = [time[0] for time in Buble]
    shell_swap = [time[0] for time in Shell]
    knuth_swap = [time[0] for time in Knuth]
    ax['S'].plot(Size, bubble_swap, Size, shell_swap)
    ax['S'].set_ylabel('Число операций обмена')
    ax['S'].set_xlabel('Размер массива')
    ax['S'].grid()
    ax['S'].legend(['Сортировка пузырьком', 'Сортировка расчёской'])

    bubble_compare = [time[1] for time in Buble]
    shell_compare = [time[1] for time in Shell]
    ax['C'].plot(Size, bubble_compare, Size, shell_compare)
    ax['C'].set_ylabel('Число операций сравнений')
    ax['C'].set_xlabel('Размер массива')
    ax['C'].grid()
    ax['C'].legend(['Сортировка пузырьком', 'Сортировка расчёской'])
    plt.show()


def new_graf2(n=100):
    degree = degree_of_sorting(n)
    Shell = []
    Buble = []
    for seq in degree[0]:
        a = seq.copy()
        b = seq.copy()
        Shell.append(brush(a))
        Buble.append(ordinary_bubble(b))

    mosaic = '''
        SC
        '''
    fig, ax = plt.subplot_mosaic(mosaic=mosaic)
    # fig, ax = plt.subplots(2, 1, layout='constrained')
    fig.suptitle('Зависимость сложности вычисления сортировки в зависимости степени отсортированности массива')

    ox = range(len(degree[0]))
    buble_swap = [time[0] for time in Buble]
    shell_swap = [time[0] for time in Shell]

    ax['S'].plot(ox, buble_swap, ox, shell_swap)
    ax['S'].set_ylabel('Число операций обмена')
    ax['S'].set_xlabel('Степень отсортированности')
    ax['S'].grid()
    ax['S'].legend(['Сортировка пузырьком', 'Сортировка расчёской', 'Сортировка Шелла с шагом Кнутта'],
                   loc='upper right')
    ax['S'].vlines(degree[1], 0, max(max(shell_swap), max(buble_swap)), colors='r')

    buble_compare = [time[1] for time in Buble]
    shell_compare = [time[1] for time in Shell]
    ax['C'].plot(ox, buble_compare, ox, shell_compare)
    ax['C'].set_ylabel('Число операций сравнений')
    ax['C'].set_xlabel('Степень отсортированности')
    ax['C'].grid()
    # ax['C'].legend(['Сортировка пузырьком', 'Сортировка расчёской', 'Сортировка Шелла с шагом Кнутта'], loc='upper right')
    ax['C'].vlines(degree[1], 0, max(max(shell_compare), max(buble_compare)), colors='r')
    plt.show()


# n = 1000
# a = list(range(n))
# random.shuffle(a)
# b = a.copy()
# # c = a.copy()
# # comb_sort(b, KnuthStep)
# # comb_sort(c, BiStep)
#
# # print(c == sorted(a))
#
# # print(a)
# # brush(b)
# # print(b)
# ordinary_bubble(b)
# print(b == sorted(a))

new_graf2(50)
# new_graf1()