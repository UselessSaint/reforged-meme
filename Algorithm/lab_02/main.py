import sys
sys.path.append("../lab_01")
from lab_01 import *
from data_generation import f


def main():
    input_data = []

    infile = open("data.txt", "r")

    for line in infile:
        arg, val = line.split()
        arg, val = float(arg), float(val)
        input_data.append([arg, val])

    infile.close()

    input_data.sort()

    n = len(input_data)
    x = float(input("Введите значение аргумента: "))

    h = [0 for _ in range(n)]
    l = [0 for _ in range(n)]
    for i in range(1, n):
        h[i] = input_data[i][0] - input_data[i - 1][0]
        l[i] = (input_data[i][1] - input_data[i - 1][1]) / h[i]

    eta = [0 for _ in range(n + 1)]
    ksi = [0 for _ in range(n + 1)]
    for i in range(2, n):
        ksi[i + 1] = h[i] / (-2 * (h[i - 1] + h[i]) - h[i] * ksi[i])
        eta[i + 1] = (h[i - 1] * eta[i] - 3 * (l[i] - l[i - 1])) / (-2 * (h[i - 1] + h[i]) - h[i] * ksi[i])

    c = [0 for _ in range(n + 1)]
    for i in range(n - 2, 1, -1):
        c[i] = ksi[i + 1] * c[i + 1] + eta[i + 1]

    a = [0] + [input_data[i - 1][1] for i in range(1, n)]
    b = [0 for _ in range(n)]
    d = [0 for _ in range(n)]
    for i in range(1, n):
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])
        b[i] = l[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3

    nearest_point = find_nearest_point(input_data, x)
    nearest_point = 1 if nearest_point == 0 else nearest_point
    if nearest_point == n + 1:
        print("Введенное значение аргумента находится за пределами исходной таблицы")

    delta = x - input_data[nearest_point - 1][0]
    sp_value = (a[nearest_point] + b[nearest_point] * delta + c[nearest_point] * delta * delta +
                d[nearest_point] * delta * delta * delta)

    print('Результат сплайн интерполяции: %.3f\n' % sp_value +
          'Результат интерполяции полиномом Ньютона: %.3f\n' % interpolate(x, 3, input_data) +
          'Истинное значение функции: %.3f\n' % f(x))


if __name__=='__main__':
    main()
