def matrix_mult(left, right):
    if isinstance(left, list) and isinstance(right, list):
        result_matrix = [[0.0 for y in range(len(right[0]))] for x in range(len(left))]
        for i in range(len(left)):
            for j in range(len(right[0])):
                for k in range(len(left)):
                    result_matrix[i][j] += left[i][k] * right[k][j]
        return result_matrix
    elif isinstance(left, list) and isinstance(right, float):
        result_matrix = [[0.0 for y in range(len(left[0]))] for x in range(len(left))]
        for i in range(len(left)):
            for j in range(len(left[0])):
                result_matrix[i][j] = left[i][j] * right
        return result_matrix


def matrix_sub(left, right):
    if isinstance(left, list) and isinstance(right, list):
        result = [[0.0 for y in range(len(left[0]))] for x in range(len(left))]
        for i in range(len(left)):
            for j in range(len(left[0])):
                result[i][j] = left[i][j] - right[i][j]
        return result


def matrix_add(left, right):
    if isinstance(left, list) and isinstance(right, list):
        result = [[0.0 for y in range(len(left[0]))] for x in range(len(left))]
        for i in range(len(left)):
            for j in range(len(left[0])):
                result[i][j] = left[i][j] + right[i][j]
        return result
