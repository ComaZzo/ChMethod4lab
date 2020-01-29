from matrix_methods import *

matrix = [
    [-0.67, 0.24, -0.48, 0.23],
    [0.72, -1.05, 0.44, 0.31],
    [0.56, -0.1, -0.97, -0.55],
    [0.47, 0.12, -0.07, -0.89]
]

result_vector = [
    [0.9], [0.7], [0.5], [0.3]
]

epsilons = [10 ** -i for i in range(2, 8)]


def gauss_method():
    matrix_copy = [[matrix[x][y] for y in range(4)] for x in range(4)]
    vector_copy = [result_vector[i][0] for i in range(4)]

    for i in range(4):
        for j in range(4):
            if i != j:
                d = matrix_copy[j][i] / matrix_copy[i][i]
                for k in range(4):
                    matrix_copy[j][k] -= matrix_copy[i][k] * d
                vector_copy[j] -= vector_copy[i] * d

    for i in range(0, 3):
        vector_copy[i] /= matrix_copy[i][i]

    print('Vector from Gauss Method:')
    print_string = str()
    for i in vector_copy:
        print_string += ('%.7f' % i) + ' '
    print(print_string[:-1])


def check(i: int, matrix_r: list):
    check1 = abs(matrix_r[0][0]) < epsilons[i]
    check2 = abs(matrix_r[1][0]) < epsilons[i]
    check3 = abs(matrix_r[2][0]) < epsilons[i]
    check4 = abs(matrix_r[3][0]) < epsilons[i]
    return check1 and check2 and check3 and check4


def speedy_descent_method():
    matrix_copy = [[matrix[x][y] for y in range(4)] for x in range(4)]
    matrix_copy_transparent = [[matrix[y][x] for y in range(4)] for x in range(4)]
    vector_copy = [[result_vector[i][0]] for i in range(4)]
    x_list = [[0.0] for i in range(4)]

    for i in range(4):
        x_list[i][0] = vector_copy[i][0] / matrix_copy[i][i]

    counter = 0
    n = 0

    b_matrix = matrix_mult(matrix_copy_transparent, matrix_copy)
    print('eps         x1           x2           x3           x4           n')

    while counter < 6:
        r_matrix = matrix_sub(matrix_mult(matrix_copy, x_list), vector_copy)

        if check(counter, r_matrix):
            print('%.7f   %.7f   %.7f   %.7f   %.7f   %d' %
                  (epsilons[counter], x_list[0][0], x_list[1][0], x_list[2][0], x_list[3][0], n))
            counter += 1
            continue

        up = 0
        down = 0
        upm = matrix_mult(b_matrix, r_matrix)
        for i in range(4):
            up += r_matrix[i][0] * upm[i][0]
            down += upm[i][0] * upm[i][0]
        u = up / down
        x_list = matrix_sub(x_list, matrix_mult(matrix_mult(matrix_copy_transparent, r_matrix), u))
        n += 1


if __name__ == '__main__':
    gauss_method()
    speedy_descent_method()
