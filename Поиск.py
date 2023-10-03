# Чтение строки t и s
def read(n=10, m=10):
    """
    Чтение файлов t.txt и s.txt
    Возвращает текст t и s в виде кортежа.
    :param n: количество строк, которые мы прочитаем в t.txt
    :return (t, s): строка t, в которой мы осуществляем поиск, и строка s, по которой мы ищем
    """
    with open('t.txt', 'r') as f:
        t = ''
        for _ in range(n):
            t += f.readline()

    with open('s.txt', 'r') as f:
        s = ''
        s += f.read(m)

    return t, s


def preprocess(pattern):
    """
    Подготовка таблицы смещений.
    :param pattern: принимает строку s
    :return table: словарь смещений
    """
    M = len(pattern)
    table = [M] * 256  # Создаем таблицу и заполняем ее длиной шаблона
    for i in range(M - 1):  # Проходим по каждому символу шаблона
        table[ord(pattern[i])] = M - 1 - i  # Записываем смещение до последнего символа шаблона
    return table


def boyer_moore_horspool(text, pattern, mode='search'):
    """
    Реализация алгоритма Бойера-Мура-Хорспула.
    :param text: строка t, по которой мы осуществляем поиск
    :param pattern: строка s, которую мы хотим найти
    :param mode: может иметь два значения: 'search' и 'count'.
    :return: если mode='search', то массив с индексами схождения pattern в text. Если mode='count',
    то возвращает количество сравнений
    """
    table = preprocess(pattern)
    M = len(pattern)
    N = len(text)
    i = M - 1  # Индекс в тексте
    j = M - 1  # Индекс в шаблоне
    k = 0  # Вспомогательный индекс, с которым мы будем искать подстроку в тексте
    matches = []  # Список для хранения индексов начала найденных подстрок
    counter = 0
    while i < N:
        if text[i - k] == pattern[j]:  # Если символы совпадают
            counter += 1
            if j == 0:  # Если это первый символ шаблона, значит мы нашли подстроку

                matches.append(i - k)  # Добавляем индекс в список
                i += M  # Смещаемся на длину шаблона
                j = M - 1  # Возвращаемся к последнему символу шаблона
            else:  # Если это не первый символ шаблона
                k += 1  # Смещаемся на один символ назад в тексте
                j -= 1  # Смещаемся на один символ назад в шаблоне
        else:  # Если символы не совпадают
            counter += 1
            i += table[ord(text[i])]  # Смещаемся на значение из таблицы смещений
            j = M - 1  # Возвращаемся к последнему символу шаблона
            k = 0
    if mode == 'search':
        return matches
    else:
        return counter


def brute_force_search(text, pattern, mode='search'):
    '''
    Реализация алгоритма грубой силы в поиске подстроки в тексте.
    :param text: строка t, по которой мы осуществляем поиск
    :param pattern: строка s, которую мы хотим найти
    :param mode: может иметь два значения: 'search' и 'count'.
    :return: если mode='search', то массив с индексами схождения pattern в text. Если mode='count',
    то возвращает количество сравнений
    '''
    N = len(text)
    M = len(pattern)
    matches = []
    counter = 0

    for i in range(N - M + 1):  # Проходим по всем возможным начальным позициям подстроки в строке
        j = 0
        while j < M and text[i + j] == pattern[j]:  # Сравниваем символы подстроки и строки
            counter += 1
            j += 1
        else:
            counter += 1

        if j == M:  # Если все символы совпали, значит подстрока найдена
            counter += 1
            matches.append(i)

    if mode == 'search':
        return matches
    else:
        return counter


import time
import matplotlib.pyplot as plt

t, s = read(100)
print(brute_force_search(t, s))
print(boyer_moore_horspool(t, s))


def graf1():
    global_times = []
    strings = [i for i in range(1, 404, 5)]

    for n in strings:
        local_time = 0
        t, s = read(n)
        ans = boyer_moore_horspool(t, s, mode='counter')
        global_times.append(ans)

    plt.plot(strings, global_times)

    global_times = []
    for n in strings:
        t, s = read(n)
        ans = brute_force_search(t, s, mode='counter')
        global_times.append(ans)

    plt.plot(strings, global_times)
    plt.xlabel('Количество поданных строк текста')
    plt.ylabel('Количество операций сравнений')
    plt.grid()
    plt.legend(['Алгоритм Бойера-Мура-Хорспула', "Алгоритм грубой силы"])
    plt.savefig('graf1123.png', format='png')
    plt.show()


def graf2():
    global_times = []
    strings = [i for i in range(1, 100, 1)]

    for m in strings:
        t, s = read(n=400, m=m)
        ans = boyer_moore_horspool(t, s, mode='counter')
        global_times.append(ans)

    plt.plot(strings, global_times)

    global_times = []
    for m in strings:
        t, s = read(n=400, m=m)
        ans = brute_force_search(t, s, mode='counter')
        global_times.append(ans)

    plt.plot(strings, global_times)
    plt.xlabel('Длина подстроки')
    plt.ylabel('Количество операций сравнений')
    plt.grid()
    plt.legend(['Алгоритм Бойера-Мура-Хорспула', "Алгоритм грубой силы"])
    plt.savefig('graf2.png', format='png')
    plt.show()



graf2()
