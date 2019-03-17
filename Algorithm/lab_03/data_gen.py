import numpy as np
import math


def z(x, y):
    return x*x + y*y


def main():
    file = open("data.txt", "w")

    while True:
        try:
            left_x = float(input("Введите левую границу для x: "))
            right_x = float(input("Введите правую границу для x: "))
            step_x = float(input("Введите шаг для x: "))

            left_y = float(input("Введите левую границу для y: "))
            right_y = float(input("Введите правую границу для y: "))
            step_y = float(input("Введите шаг для y: "))
            break
        except ValueError:
            print("Значения должны быть вещественными числами.")

    x_values = np.arange(left_x, right_x + step_x/2, step_x)
    y_values = np.arange(left_y, right_y + step_y/2, step_y)
    z_values = [[] for _ in range(len(y_values))]
    for i in range(len(y_values)):
        for j in range(len(x_values)):
            z_values[i].append(round(z(x_values[j], y_values[i]), 3))

    max_len = 0
    for i in x_values:
        if len(str(i)) > max_len:
            max_len = len(str(i))

    for i in y_values:
        if len(str(i)) > max_len:
            max_len = len(str(i))

    for i in range(len(z_values)):
        for j in range(len(z_values[i])):
            if len(str(z_values[i][j])) > max_len:
                max_len = len(str(z_values[i][j]))

    format_str = "%"+str(max_len)+"s "
    file.write(format_str % -0.0)

    for i in x_values:
        file.write(format_str % i)
    file.write("\n")

    for i in range(len(y_values)):
        file.write(format_str % y_values[i])
        for j in range(len(z_values[i])):
            file.write(format_str % z_values[i][j])
        file.write("\n")
    file.close()


if __name__ == '__main__':
    main()
