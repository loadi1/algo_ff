import matplotlib.pyplot as plt


def read(n=5, counting='counting', quick1='quick1', quick2='quick2'):
    with open(f'{counting}.txt', 'r') as f:
        counting = []
        for _ in range(n):
            counting.append(float(f.readline()))

    with open(f'{quick1}.txt', 'r') as f:
        quick1 = []
        for _ in range(n):
            quick1.append(float(f.readline()))

    with open(f'{quick2}.txt', 'r') as f:
        quick2 = []
        for _ in range(n):
            quick2.append(float(f.readline()))

    return counting, quick1, quick2


def graf1(counting, quick1, quick2):
    n = len(counting)

    fig, ax = plt.subplots()
    ax.plot(range(n), counting, range(n), quick1, range(n), quick2)
    ax.set_xlabel('Количество символов')
    ax.set_ylabel('Время работы, миллисекунд')
    ax.set_title('Сравнение времени работы')
    ax.legend(['CouningSort', 'QuickSort1', 'QuickSort2'])
    plt.savefig('CountingSort_VS_QuickSort1_VS_QuickSort2.png', format='png')
    plt.show()


# добавить на график односторонний двухсторонний квиксорт
def graf2(counting, quick1, quick2):
    n = len(counting)

    fig, ax = plt.subplots()
    ax.plot(range(n), counting, range(n), quick1, range(n), quick2)
    ax.set_xlabel('Степень отсортированности')
    ax.set_ylabel('Время работы, миллисекунд')
    ax.set_title('Сравнение времени работы')
    ax.legend(['CouningSort', 'QuickSort1', 'QuickSort2'])
    plt.savefig('CountingSort_VS_QuickSort1_VS_QuickSort2_degree.png', format='png')
    plt.show()


# graf1(*read(9995))

graf2(*read(1950 - 5, 'counting_dergee', 'quick1_dergee_new', 'quick2_degree_new'))
