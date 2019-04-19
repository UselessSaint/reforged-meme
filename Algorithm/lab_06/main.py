import numpy as np
from math import cos


def f(x):
    # return x*x
    return x/(1+2*x)


def load_data_into_file(data):
    length = len(data[0])

    file = open("data.txt", "w")

    labels = ["X", "Y", "1", "2", "3", "4", "5"]

    for i in labels:
        file.write("%8s|" % i)
    file.write("\n")

    for i in range(length):
        for j in range(len(data)):
            if type(data[j][i]) != str:
                file.write("%8s|" % round(data[j][i], 3))
            else:
                file.write("%8s|" % data[j][i])
        file.write("\n")

    file.close()


def find_first_column(x, y):
    result = list()

    for i in range(len(x) - 1):
        result.append((y[i+1] - y[i]) /
                      (x[i+1] - x[i]))

    result.append("---")

    return result


def find_second_column(x, y):
    result = list()

    result.append("---")

    for i in range(1, len(x) - 1):
        result.append((y[i+1] - y[i-1]) /
                      (x[i+1] - x[i-1]))

    result.append("---")

    return result


def find_fourth_column(x, y):
    result = list()

    for i in range(len(x) - 2):
        cur_div = ((y[i+1] - y[i]) /
                   (x[i+1] - x[i]))

        cur_div -= ((y[i+2] - y[i]) /
                    (x[i+2] - x[i]))

        cur_div += ((y[i+1] - y[i]) /
                    (x[i+1] - x[i]))

        result.append(cur_div)

    result.append("---")
    result.append("---")

    return result


def find_third_column(x, y):
    result = list()

    result.append((-3*y[0] + 4*y[1] - y[2])/(x[2] - x[0]))

    for i in range(1, len(x) - 1):
        result.append("---")

    result.append((-4*y[-2] + y[-3] + 3*y[-1])/(x[-1] - x[-3]))

    return result


def main():
    x = np.arange(0, 12, 1)
    y = [f(i) for i in x]

    first = find_first_column(x, y)
    second = find_second_column(x, y)
    third = find_third_column(x, y)
    fourth = find_fourth_column(x, y)

    load_data_into_file([x, y, first, second, third, fourth])


if __name__ == '__main__':
    main()
