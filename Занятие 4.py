'''
quick sort
выберем случайный эелемент в массиве
Двигаемся с начала и до тех пор, пока a_i < x. нашли
потом с конца двигаем пока не найдём a_j > x. Меняем a_i и a_j
'''


def quick_sort(a, l, r):
    def swap(m, i, j):
        pass

    i = l
    j = r
    x = (l + r) // 2
    while j < j:
        while a[i] < x and i < j:
            i += 1
        while a[j] >= x and i < j:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]
            break
    # Добавить сравнение
    if l < j:
        quick_sort(a, r, j)
    if i < r:
        quick_sort(a, i, r)


G = 0
def quick_sort_gpt(arr):
    global G
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    G += len(left)
    middle = [x for x in arr if x == pivot]
    G += len(middle)
    right = [x for x in arr if x > pivot]
    G += len(right)

    return quick_sort_gpt(left) + middle + quick_sort_gpt(right)

import random
a = [random.random() for _ in range(1000)]
print(len(a))
a_sort = quick_sort_gpt(a)
print(a_sort)
print(G)


"""Большие массивы, делим на две части и распихиваем две системы. Читаем верхушки. Результат записываем на две выходные 
ленты в равные части. Сравнили пары в конце концов. Потом заново, но сравнимаем четвёрки"""

#
