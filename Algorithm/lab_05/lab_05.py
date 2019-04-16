from lab_01 import *
from math import pow, exp, log


Q_data = [[2000,   4000,   6000,   8000,   10000,  12000,  14000,  16000,  18000,  20000,  22000,  24000,  26000],
          [1.0000, 1.0000, 1.0000, 1.0001, 1.0025, 1.0198, 1.0895, 1.2827, 1.6973, 2.4616, 3.3652, 5.3749, 7.6838],
          [4.0000, 4.0000, 4.1598, 4.3006, 4.4392, 4.5661, 4.6817, 4.7923, 4.9099, 5.0511, 5.2354, 5.4841, 5.8181],
          [5.5000, 5.5000, 5.5116, 5.9790, 6.4749, 6.9590, 7.4145, 7.8370, 8.2289, 8.5970, 8.9509, 9.3018, 9.6621],
          [11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000],
          [15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000]]

P_mind = 0
P_maxd = 20
Eps = 1e-1

Z_c = [0, 1, 2, 3, 4]
E_c = [12.13, 20.98, 31.00, 45.00]


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


def approximated_Nt(T, P):
    return 7243*P/T


def t(z, T0, Tw, m):
    return T0 + (Tw - T0)*pow(z, m)


def find_d_e(T, gamma):
    d_e = list()

    for i in range(4):
        d_e_i = 8.61*pow(10, -5)*T*log((1 + Z_c[i+1]*Z_c[i+1]*gamma/2) * (1+gamma/2) /
                     (1+Z_c[i]*Z_c[i]*gamma/2))

        d_e.append(d_e_i)

    return d_e


def find_K(T, d_e):
    K = list()

    for i in range(4):
        Q_ip1 = interpolate_2_lists(T, 4, Q_data[0], Q_data[i+2])
        Q_i = interpolate_2_lists(T, 4, Q_data[0], Q_data[i+1])

        K_i = 2*2.415*pow(10, -3) * (Q_ip1/Q_i) * pow(T, 3/2) * exp(-E_c[i]+d_e[i])*11603/T

        K.append(K_i)

    return K


def gamma_func(gamma, T, X):
    right_part = X[0]/(1+gamma/2)

    for i in range(2, 6):
        right_part += ((exp(X[i])*Z_c[i-1]*Z_c[i-1]) /
                       (1+Z_c[i-1]*Z_c[i-1]*gamma/2))

    right_part *= 5.87*pow(10, 10)/pow(T, 3)

    return gamma*gamma - right_part


def find_gamma(st, end, T, X):
    while abs(st-end) > Eps:
        cur_gamma = (st+end)/2

        if gamma_func(cur_gamma, T, X) <= 0:
            st = cur_gamma
        else:
            end = cur_gamma

    return (st+end)/2


def find_max_increment(X, d_X):
    max_inc = abs(d_X[0]/X[0])
    for i in range(1, len(X)):
        if abs(d_X[i]/X[i]) > max_inc:
            max_inc = abs(d_X[i]/X[i])
    return max_inc


def Nt(T, P):
    X = [-1, 3, -1, -20, -20, -20]

    while True:
        gamma = find_gamma(0, 3, T, X)
        d_e = find_d_e(T, gamma)
        K = find_K(T, d_e)

        lin_sys_left_side = [[1, -1, 1, 0, 0, 0],
                             [1, 0, -1, 1, 0, 0],
                             [1, 0, 0, -1, 1, 0],
                             [1, 0, 0, 0, -1, 1],
                             [-exp(X[0]), -exp(X[1]), -exp(X[2]), -exp(X[3]), -exp(X[4]), -exp(X[5])],
                             [exp(X[0]), 0, -Z_c[1]*exp(X[2]), -Z_c[2]*exp(X[3]), -Z_c[3]*exp(X[4]), -Z_c[4]*exp(X[5])]]

        alpha = 0.285*pow(10, -11)*pow(gamma*T, 3)

        lin_sys_right_side = [log(K[0])+X[1]-X[2]-X[0],
                              log(K[1])+X[2]-X[3]-X[0],
                              log(K[2])+X[3]-X[4]-X[0],
                              log(K[3])+X[4]-X[5]-X[0],
                              exp(X[0])+exp(X[1])+exp(X[2])+exp(X[3])+exp(X[4])+exp(X[5])-alpha-P*7243/T,
                              Z_c[1]*exp(X[2])+Z_c[2]*exp(X[3])+Z_c[3]*exp(X[4])+Z_c[4]*exp(X[5])-exp(X[0])]

        d_X = solve_lin_system_gauss(lin_sys_left_side, lin_sys_right_side)

        if find_max_increment(X, d_X) < Eps:
            break

        for i in range(len(X)):
            X[i] += d_X[i]

    return sum([exp(i) for i in X])


def main():
    P_max = P_maxd
    P_min = P_mind

    P0 = float(input("P0: "))
    T0 = float(input("T0: "))
    Tw = float(input("Tw: "))
    m = float(input("m: "))

    while abs(P_max - P_min)  > Eps:
        curr_p = abs(P_max-P_min)/2.0
        curr_p+=P_min

        integral_value = integrate(0, 1, lambda z: Nt(t(z, T0, Tw, m), curr_p)*z)

        if (approximated_Nt(T0, P0)-2*integral_value) >= 0:
            P_min = curr_p
        else:
            P_max = curr_p

    print("Result: ", P_max)


if __name__=='__main__':
    main()
