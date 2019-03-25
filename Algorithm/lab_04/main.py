import math


def fi(x, coefs):
    result = 0
    for i in range(len(coefs)):
        result += x**i * coefs[i]
        print(coefs[i], x**i)

    return result


def scalar_mult(power1, data1, power2, data2, weights):
    result = 0

    for i in range(len(data1)): # cos data1 and data 2 have same len
        mult = math.pow(data1[i], power1)*math.pow(data2[i], power2)*weights[i]
        result += mult

    return result


def solve_slay_gaus(mtr, left_side):
    n = len(mtr) # in this problem we'r only have square matrix
    for i in range(0, n):
        for j in range(i+1, n):
            sep = mtr[j][i] / mtr[i][i]
            for k in range(0, n):
                mtr[j][k] -= mtr[i][k] * sep
            left_side[j] -= left_side[i] * sep

    left_side[n-1] = left_side[n-1] / mtr[n-1][n-1]

    for i in range(n-2, -1, -1):
        for k in range(i+1, n):
            left_side[i] -= mtr[i][k] * left_side[i+1]
        left_side[i] /= mtr[i][i]

    return left_side


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
            xf = float(input("Введите x: "))
            break
        except ValueError:
            print("n должно быть действительным числом.")

    coef_mtr = [[] for _ in range(n+1)]
    left_side_list = []

    for i in range(n+1):
        for j in range(n+1):
            coef_mtr[i].append(scalar_mult(i, x, j, x, w))
        left_side_list.append(scalar_mult(1, y, i, x, w))

    # [print(i) for i in coef_mtr]
    # print(left_side_list)

    coefs = solve_slay_gaus(coef_mtr, left_side_list)
    print(coefs)
    print(fi(xf, coefs))


if __name__=='__main__':
    main()
