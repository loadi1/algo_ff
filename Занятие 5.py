'''
Полифазная сортировка слиянием

MathSort(int x[1 : N], int y[1:N], int f(int)):

'''

def MathSort(int x[1 : N], int y[1:N], int f(int)):
    int t[0:k-1] = [0]*k
    for i in range(N):
        j = f(x[i])
        t[j]++

    for i in range(k-2, -1, -1):
        t[i]+=t[i+1]

    for i in range(1, n+1):
        j = f(x[i])

        y[n+1-t[j]] = x[i]
        t[j]--

# сравнить сортировку подсчётом с квиссортом (случайные числа (реально) целевая функция время, f() - заполняется таблицу в прямом порядке и в обратном
