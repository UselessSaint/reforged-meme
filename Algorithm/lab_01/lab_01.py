import numpy as np
import math

from data_generation import f


def find_nearest_point(input_data, x):
    indata_len = len(input_data)

    lower = 0
    upper = indata_len

    while abs(upper - lower) > 1:
        if input_data[(lower + upper)//2][0] > x:
            upper = (lower + upper)//2
        elif input_data[(lower + upper)//2][0] < x:
            lower = (lower + upper)//2
        elif input_data[(lower + upper)//2][0] == x:
            return (lower + upper)//2

    if abs(x - upper) > abs(x - lower):
        result = lower
    else:
        result = upper

    return result


def find_nearest_pointt(input_data, x):
    indata_len = len(input_data)

    current_diff = abs(input_data[0][0] - x)
    result = 0

    for i in range(1, indata_len):
        if abs(input_data[i][0] - x) < current_diff:
            result = i
            current_diff = abs(input_data[i][0] - x)

    return result

def find_div_diff(input_data, lower_edge, upped_edge):
    n = upped_edge - lower_edge
    div_diff = [[] for i in range(n + 1)]

    for i in range(lower_edge, upped_edge + 1):
        div_diff[0].append(input_data[i][1])

    for i in range(1, n + 1):
        for j in range(n + 1 - i):
            tmp = input_data[i + j + lower_edge][0] - input_data[j + lower_edge][0]
            # print(tmp)
            if tmp == 0:
                div_diff[i].append(0.0)
                continue
                #tmp = 1e-10
            div_diff[i].append((div_diff[i - 1][j + 1] - div_diff[i - 1][j])/(tmp))

    # [print(div_diff[i]) for i in range(len(div_diff))]

    return div_diff


def find_value(x, div_diff, input_data):
    result = 0
    n = len(div_diff)

    for i in range(n):
        tmp = 1
        for j in range(i):
            tmp *= x - input_data[j][0]
        tmp *= div_diff[i][0]

        result += tmp

    return result


def interpolate(x, n, input_data):
    if n + 1 > len(input_data):
        n = len(input_data) - 1

    nearest_point = find_nearest_point(input_data, x)
    # print(nearest_point, input_data[nearest_point][0])
    # print(find_nearest_pointt(input_data, x), input_data[find_nearest_pointt(input_data, x)][0])
    indata_len = len(input_data)
    upped_edge, lower_edge = nearest_point, nearest_point

    amount_of_points = n

    if amount_of_points > indata_len:
        amount_of_points = indata_len

    while amount_of_points > 0:
        if upped_edge < indata_len - 1:
            upped_edge += 1
            amount_of_points -= 1
        if amount_of_points > 0 and lower_edge > 0:
            lower_edge -= 1
            amount_of_points -= 1

    div_diff = find_div_diff(input_data, lower_edge, upped_edge)

    value = find_value(x, div_diff, input_data[lower_edge:upped_edge])

    return value


def main():
    input_data = []

    infile = open("data.txt", "r")

    for line in infile:
        arg, val = line.split()
        arg, val = float(arg), float(val)
        input_data.append([arg, val])

    infile.close()

    while True:
        try:
            n = int(input("Введите степень полинома: "))
            x = float(input("Введите значение аргумента: "))
            break
        except ValueError:
            print("Степень должна быть натуральным числом.")
            print("Значение должно быть вещественным числом.")

    input_data.sort()

    value = interpolate(x, n, input_data)

    print("Результат работы: {:f}\nИстинное значение: {:f}".format(value, f(x)))

    # root_data = [[i[1],i[0]] for i in input_data]
    # print(input_data)
    # print(root_data)

    root_data = []

    for i in range(len(input_data)):
        root_data.append([input_data[i][1],input_data[i][0]])

    # root_data.sort()
    # print(root_data)

    root = interpolate(0, n, root_data)
    print("Корень: ", root)
    print("Значение в найденном корне: ", f(root))


if __name__ == "__main__":
    main()