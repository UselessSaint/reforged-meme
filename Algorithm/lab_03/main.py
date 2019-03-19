import sys
sys.path.append("../lab_01")
from lab_01 import *
from data_gen import z


def find_nearest_points_xy(in_data, x, y):
    in_data_len = len(in_data)

    lower = 1
    upper = in_data_len

    while abs(upper - lower) > 1:
        if in_data[0][(lower + upper)//2] > x:
            upper = (lower + upper)//2
        elif in_data[0][(lower + upper)//2] <= x:
            lower = (lower + upper)//2
        # elif in_data[(lower + upper)//2][0] == x:
        #     near_x = (lower + upper)//2

    # try:
    #     if abs(x - in_data[0][upper]) > abs(x - in_data[0][lower]):
    #         near_x = lower
    #     else:
    #         near_x = upper
    # except IndexError:
    near_x = lower

    lower = 1
    upper = in_data_len

    while abs(upper - lower) > 1:
        if in_data[(lower + upper)//2][0] > y:
            upper = (lower + upper)//2
        elif in_data[(lower + upper)//2][0] <= y:
            lower = (lower + upper)//2

    # try:
    #     if abs(y - in_data[upper][0]) > abs(y - in_data[lower][0]):
    #         near_y = lower
    #     else:
    #         near_y = upper
    # except IndexError:
    near_y = lower

    return near_x, near_y


def main():
    in_data = []

    in_file = open("data.txt", "r")

    for line in in_file:
        in_data.append(list(map(float, line.split())))

    in_file.close()

    while True:
        try:
            xn = int(input("Введите степень полинома для х: "))
            x = float(input("Введите значение аргумента x: "))

            yn = int(input("Введите степень полинома для y: "))
            y = float(input("Введите значение аргумента y: "))
            break
        except ValueError:
            print("Степень должна быть натуральным числом.")
            print("Значение должно быть вещественным числом.")

    near_x, near_y = find_nearest_points_xy(in_data, x, y)

    up_edge_x, low_edge_x = near_x, near_x
    up_edge_y, low_edge_y = near_y, near_y

    amnt_of_p_x = xn
    amnt_of_p_y = yn

    len_x_data = len(in_data[0]) - 1
    len_y_data = len(in_data) - 1

    # print(len_x_data, len_y_data)

    while amnt_of_p_x > 0:
        if up_edge_x < len_x_data:
            up_edge_x += 1
            amnt_of_p_x -= 1
        if amnt_of_p_x > 0 and low_edge_x > 0:
            low_edge_x -= 1
            amnt_of_p_x -= 1

    while amnt_of_p_y > 0:
        if up_edge_y < len_y_data:
            up_edge_y += 1
            amnt_of_p_y -= 1
        if amnt_of_p_y > 0 and low_edge_y > 0:
            low_edge_y -= 1
            amnt_of_p_y -= 1

    # print(up_edge_x, low_edge_x, in_data[0][up_edge_x], in_data[0][low_edge_x])
    # print(up_edge_y, low_edge_y, in_data[up_edge_y][0], in_data[low_edge_y][0])

    y_values = [in_data[i][0] for i in range(len(in_data))]
    x_values = [in_data[0][i] for i in range(1, len(in_data))]

    zy = []
    cur_table = []

    for j in range(low_edge_y, up_edge_y + 1):
        for i in range(len(x_values)):
            z_values = in_data[j][1:]
            cur_table = [[x_values[i], z_values[i]] for i in range(low_edge_x-1, up_edge_x)]
        zy.append(interpolate(x, xn, cur_table))
        # print(interpolate(x, xn, cur_table))

    y_values = y_values[low_edge_y:up_edge_y+1]
    cur_table = [[y_values[i], zy[i]] for i in range(len(zy))]

    # print(interpolate(y, yn, cur_table), z(x, y))

    print("Результат работы: %.3f\n" % interpolate(y, yn, cur_table) +
          "Истинное значение: %.3f" % z(x,y))


if __name__ == '__main__':
    main()
