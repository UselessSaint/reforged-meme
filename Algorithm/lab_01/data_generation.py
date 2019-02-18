import math
import numpy as np


def f(x):
    return x*x*x - 1
    # return math.cos(math.pi/2*x)


def generate_data():
    file = open("data.txt", "w")

    while True:
        try:
            left_border = float(input("Введите левую границу значений изначальной таблицы: "))
            right_border = float(input("Введите правую границу значений изначальной таблицы: "))

            step = float(input("Введите шаг: "))

            break
        except ValueError:
            print("Значения должны быть вещественными числами.")

    x_values = np.arange(left_border, right_border + step/2, step)

    for i in x_values:
        file.write("{:.3f} {:.3f}\n".format(i, f(i)))

    file.close()


def main():
    generate_data()


if __name__ == "__main__":
    main()