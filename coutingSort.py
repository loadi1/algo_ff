import matplotlib.pyplot as plt


def read(n=5):
    with open('counting.txt', 'r') as f:
        counting = []
        for _ in range(n):
            counting.append(float(f.readline()))

    with open('quick.txt', 'r') as f:
        quick = []
        for _ in range(n):
            quick.append(float(f.readline()))

    return counting, quick


def graf1(counting, quick):
    n = len(counting)

    fig, ax = plt.subplots()
    ax.plot(range(n), counting, range(n), quick)
    ax.set_xlabel('Количество символов')
    ax.set_ylabel('Время работы, миллисекунд')
    ax.set_title('Сравнение времени работы')
    ax.legend(['CouningSort', 'QuickSort'])
    plt.savefig('CountingSort_VS_QuickSort.png', format='png')
    plt.show()

graf1(*read(10000-5))
