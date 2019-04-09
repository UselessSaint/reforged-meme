import math
import matplotlib.pyplot as plt
import numpy as np


def draw_grag(coefs, xdata, ydata):
    cx = np.arange(xdata[0], xdata[-1] + 1e-10, 0.1)
    x = list()
    y = list()
    for i in cx:
        x.append(i)
        y.append(fi(i, coefs))

    plt.plot(x, y)
    for i in range(len(xdata)):
        plt.scatter(x=xdata[i], y=ydata[i], alpha=0.3)
    plt.show()


def fi(x, coefs):
    result = 0
    for i in range(len(coefs)):
        result += x**i * coefs[i]

    return result


def scalar_mult(power1, data1, power2, data2, weights):
    result = 0

    for i in range(len(data1)): # cos data1 and data 2 have same len
        mult = math.pow(data1[i], power1)*math.pow(data2[i], power2)*weights[i]
        result += mult

    return result


def solve_slay_gaus(left_side, right_side):
    n = len(left_side)
    for i in range(0, n):
        for j in range(i+1, n):
            sep = left_side[j][i]/left_side[i][i]
            for k in range(0, n):
                left_side[j][k] -= left_side[i][k] * sep
            right_side[j] -= right_side[i] * sep

    for i in range(n-1, -1, -1):
        for k in range(i+1, n):
            right_side[i] -= left_side[i][k] * right_side[k]
        right_side[i] /= left_side[i][i]

    return right_side


def main():
    input_file = open("data.txt", "r")

    x, y, w = list(), list(), list() # x, y - coordinates, w - weight

    for line in input_file:
        line = list(map(float,line.split()))
        x.append(line[0])
        y.append(line[1])
        w.append(line[2])

    input_file.close()

    while True:
        try:
            n = int(input("Введите n: "))
            # xf = float(input("Введите x: "))
            break
        except ValueError:
            print("n должно быть действительным числом.")

    coef_mtr = [[] for _ in range(n+1)]
    left_side_list = []

    for i in range(n+1):
        for j in range(n+1):
            coef_mtr[i].append(scalar_mult(i, x, j, x, w))
        left_side_list.append(scalar_mult(1, y, i, x, w))

    coefs = solve_slay_gaus(coef_mtr, left_side_list)

    draw_grag(coefs, x, y)

    # print(fi(xf, coefs))
    # print(math.cos(xf))


if __name__=='__main__':
    main()
