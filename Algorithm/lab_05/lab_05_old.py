from lab_01 import *
from math import pow, exp, log, sqrt, isnan
from scipy.optimize import bisect


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


def find_d_e(t, gamma, z_consts, i):
    result = 8.61*pow(10, -5)*t
    result *= log( (1+pow(z_consts[i+1], 2)*gamma/2) * (1+gamma/2) / (1+pow(z_consts[i], 2)*gamma/2))

    return result


def find_k_i(Q_data, t, e_consts, d_e, i):
    result = 2*2.415*pow(10, -3)

    Q_ip1 = interpolate_2_lists(t, 4, Q_data[0], Q_data[i+2])
    Q_i = interpolate_2_lists(t, 4, Q_data[0], Q_data[i+1])

    result *= Q_ip1/Q_i
    result *= pow(t, 3/2)

    result *= exp(-(e_consts[i]-d_e[i])*11603/t)

    return result


def find_gamma(st, end, t, X, z_consts, Eps):
    while abs(st-end) > Eps:
        curr_g = (st + end) / 2
        print(st, end, curr_g)
        result = 0
        brackets = 0

        result = 5.87*pow(10, 10)/pow(t, 3)

        brackets = exp(X[0])/(1+curr_g/2)
        for i in range(2, 6):
            brackets += (exp(X[i])*pow(z_consts[i-1], 2)) / (1+pow(z_consts[i-1], 2)*curr_g/2)

        result *= brackets

        if (curr_g*curr_g - result) >= 0:
            st = curr_g
        else:
            end = curr_g
    print(st)
    return st


def find_gamma(gamma, t, X, z_consts):
    result = 5.87*pow(10, 10)/pow(t, 3)

    brackets = exp(X[0])/(1+gamma/2)
    for i in range(2, 6):
        brackets += (exp(X[i])*pow(z_consts[i-1], 2)) / (1+pow(z_consts[i-1], 2)*gamma/2)

    result *= brackets

    return gamma*gamma - result


def find_max_increment(X, d_X):
    max_inc = abs(X[0]/d_X[0])
    for i in range(1, len(X)):
        if abs(d_X[i]/X[i]) > max_inc:
            max_inc = abs(X[i]/d_X[i])
    return max_inc


def nt(t, p, Q_data, Eps):
    # gamma = 0
    e_consts = [12.13, 20.98, 31.00, 45.00]
    z_consts = [0, 1, 2, 3, 4]
    X = [-1, 3, -1, -20, -20, -20]
    d_X = [Eps for _ in range(6)]
    # print(find_max_increment(X, d_X))
    #while find_max_increment(X, d_X) > Eps:
    for i in range(1):
        #gamma = find_gamma(0, 10, t, X, z_consts, Eps)
        #d_e = [find_d_e(t, gamma, z_consts, i) for i in range(0, 4)]
        K = [find_k_i(Q_data, t, e_consts, d_e, i) for i in range(0, 4)]
        print(K)

        lin_sys_left_side = [[1, -1, 1, 0, 0, 0],
                             [1, 0, -1, 1, 0, 0],
                             [1, 0, 0, -1, 1, 0],
                             [1, 0, 0, 0, -1, 1],
                             [exp(X[0])] + [-z_consts[i-1]*exp(X[i]) for i in range(1, 6)],
                             [exp(X[0])] + [exp(X[i]) for i in range(1, 6)]]

        # print(gamma)
        alpha = 0.285*pow(10, -11)*pow(gamma*t, 3)

        lin_sys_right_side = [log(K[0]) + X[1] - X[2] - X[0],
                              log(K[1]) + X[2] - X[3] - X[0],
                              log(K[2]) + X[3] - X[4] - X[0],
                              log(K[3]) + X[4] - X[5] - X[0],
                              sum([z_consts[i-1]*exp(X[i]) for i in range(1, 6)]) - exp(X[0]),
                              sum([exp(X[i]) for i in range(1, 6)]) + exp(X[0]) - 7243*p/t - alpha]

        d_X = solve_lin_system_gauss(lin_sys_left_side, lin_sys_right_side)
        if isnan(d_X[0]):
            break
        # print(X)
        X = [X[i] + d_X[i] for i in range(len(d_X))]
        # print(X)

    # print(X)
    # print("------")
    # print(d_X)
    # print("------")
    # print(d_e)
    # print("------")
    # print(K)
    # print("------")
    # [print(i) for i in lin_sys_left_side]
    return X


def main():
    global Q_data, P_min, P_max, Eps

    P0 = 1  # float(input("P0: "))
    T0 = 1000  # float(input("T0: "))
    Tw = 2000  # float(input("Tw: "))
    m = 0  # float(input("m: "))

    res = nt(T0, 1, Q_data, Eps)
    # print(res)
    # res = [exp(i) for i in res]
    # print(sum(res))

    # while abs(P_max - P_min) > Eps:
    #     curr_p = abs(P_max + P_min) / 2.0
    #
    #     integral_value = integrate(0, 1, lambda z: approximated_nt(t(z, T0, Tw, m), curr_p)*z)
    #
    #     if (approximated_nt(T0, P0) - 2*integral_value) >= 0:
    #         P_min = curr_p
    #     else:
    #         P_max = curr_p
    #
    # print("Result: ", P_max)


if __name__ == '__main__':
    main()

