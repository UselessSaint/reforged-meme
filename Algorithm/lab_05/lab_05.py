from lab_01 import *
from math import pow


Q_data = [[2000,   4000,   6000,   8000,   10000,  12000,  14000,  16000,  18000,  20000,  22000,  24000,  26000],
          [1.0000, 1.0000, 1.0000, 1.0001, 1.0025, 1.0198, 1.0895, 1.2827, 1.6973, 2.4616, 3.3652, 5.3749, 7.6838],
          [4.0000, 4.0000, 4.1598, 4.3006, 4.4392, 4.5661, 4.6817, 4.7923, 4.9099, 5.0511, 5.2354, 5.4841, 5.8181],
          [5.5000, 5.5000, 5.5116, 5.9790, 6.4749, 6.9590, 7.4145, 7.8370, 8.2289, 8.5970, 8.9509, 9.3018, 9.6621],
          [11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000],
          [15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000]]

P_min = 0
P_max = 20
Eps = 1e-10


def solve_lin_system_gauss(left_side, right_side):
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


def interpolate_2_lists(x, n, list1, list2):
    length = len(list1)

    input_data = [[] for _ in range(length)]

    for i in range(length):
        input_data[i].append(list1[i])
        input_data[i].append(list2[i])

    result = interpolate(x, n, input_data)

    return result


def integrate(st, end, function):
    step = 0.01
    result = 0

    while st <= end:
        left = function(st)
        st += step
        right = function(st)

        result += step*(left + right)/2

    return round(result, 4)


def t(z, t0, tw, m):
    return t0 + (tw - t0)*pow(z, m)


def approximated_nt(t, p):
    return 7243*p/t


def main():
    global Q_data, P_min, P_max, Eps

    P0 = 1  # float(input("P0: "))
    T0 = 1000  # float(input("T0: "))
    Tw = 2000  # float(input("Tw: "))
    m = 0  # float(input("m: "))

    while abs(P_max - P_min) > Eps:
        curr_p = abs(P_max - P_min) / 2.0
        curr_p += P_min

        integral_value = integrate(0, 1, lambda z: approximated_nt(t(z, T0, Tw, m), curr_p)*z)

        if (approximated_nt(T0, P0) - 2*integral_value) >= 0:
            P_min = curr_p
        else:
            P_max = curr_p

    print("Result: ", P_max)


if __name__ == '__main__':
    main()

