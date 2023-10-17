from math import sqrt

matrix = list[list[float]]
vector = list[float]


def get_condition_value(vector_1: vector, vector_0: vector, q_value: float, approximation_error: float) -> bool:
    count: int = len(vector_1)
    current_vector: vector = [abs(vector_1[index] - vector_0[index]) for index in range(count)]
    infinity_matrix_norm: float = max(current_vector)

    return q_value / (1 - q_value) * infinity_matrix_norm > approximation_error


def print_result(iteration_count: int, result_vector: vector) -> None:
    count: int = len(result_vector)
    print(f"Numarul de iteratii: {iteration_count}")

    for index in range(count):
        print(f"x{index + 1} = {result_vector[index]}")


def transforma1(pp, matrice: matrix):
    for i in range(len(matrice[0])):

        if matrice[pp][pp] != 1:
            q00 = matrice[pp][pp]

            for j in range(len(matrice[0])):
                matrice[pp][j] = matrice[pp][j] / q00


def transforma0(r, c, matrice: matrix):
    for i in range(len(matrice[0])):
        if matrice[r][c] != 0:
            q04 = matrice[r][c]

            for j in range(len(matrice[0])):
                print('r = ', r, 'j = ', j, 'c = ', c)
                print('matrice[r][j] = ', matrice[r][j])
                print('matrice[c][j] = ', matrice[c][j])
                matrice[r][j] = matrice[r][j] - ((q04) * matrice[c][j])


def gauss_method(system_matrix: matrix):
    local_matrix: matrix = system_matrix.copy()
    count = len(local_matrix)

    for i in range(count):
        transforma1(i, local_matrix)

        for j in range(count):
            if j > i:
                transforma0(j, i, local_matrix)

    x = list(range(count))

    for i in range(count, 0, -1):
        x[i - 1] = local_matrix[i - 1][4]

        for j in range(count):
            if j != (i - 1):
                x[i - 1] -= x[j] * local_matrix[i - 1][j]

    for i in range(count):
        print(f"x{i + 1} = {x[i]}")
    print("\n", end="")


def cholesky_method(system_matrix: matrix):
    local_matrix: matrix = system_matrix.copy()
    count: int = len(local_matrix)

    matrix_l: matrix = [[0] * count] * count

    for i in range(count):

        for j in range(i + 1):
            local_sum: float = 0

            if j == i:

                for k in range(j):
                    local_sum += matrix_l[j][k] ** 2

                matrix_l[j][j] = sqrt(local_matrix[j][j] - local_sum)

            else:

                for k in range(j):
                    local_sum += (matrix_l[i][k] * matrix_l[j][k])

                if (matrix_l[j][j] > 0):
                    matrix_l[i][j] = (local_matrix[i][j] - local_sum) / matrix_l[j][j]

    y = []

    for i in range(len(local_matrix)):
        y.append(vector_b[i] / matrix_l[i][i])

    x = []

    for i in range(len(local_matrix)):
        x.append(y[i] / matrix_l[i][i])

    for i in range(len(x)):
        print(f"x{i + 1} = {x[i]}")
    print("\n", end="")


def jacobi_method(local_matrix: matrix, local_vector: vector, approximation_error: float):
    count: int = len(local_matrix)
    iteration_count: int = 0

    matrix_q: matrix = [[0] * count] * count
    matrix_q_abs: vector = [0] * count ** 2

    for first_index in range(count):
        for second_index in range(count):
            if first_index != second_index:
                matrix_q[first_index][second_index] = - local_matrix[first_index][second_index] / \
                                                      local_matrix[first_index][first_index]

            matrix_q_abs.append(abs(matrix_q[first_index][second_index]))

    q_value: float = max(matrix_q_abs)

    vector_c: vector = [local_vector[index] / local_matrix[index][index] for index in range(count)]

    initial_vector_x: vector = vector_c
    current_vector_x: vector = initial_vector_x.copy()

    condition: bool = True

    while (condition):
        iteration_count += 1
        current_vector_x = initial_vector_x.copy()

        for index in range(count):
            for second_index in range(count):
                current_vector_x[index] = current_vector_x[index] + matrix_q[first_index][second_index] * \
                                          initial_vector_x[second_index]

        condition = get_condition_value(current_vector_x, initial_vector_x, q_value, approximation_error)
        initial_vector_x = current_vector_x.copy()

    print_result(iteration_count, current_vector_x)


def gauss_seidel_method(local_matrix: matrix, local_vector: vector, approximation_error: float):
    count: int = len(local_matrix)
    iteration_count: int = 0

    matrix_q: matrix = [[0] * count] * count
    matrix_q_abs: vector = [0] * count ** 2

    for first_index in range(count):
        for second_index in range(count):
            if first_index != second_index:
                matrix_q[first_index][second_index] = - local_matrix[first_index][second_index] / \
                                                      local_matrix[first_index][first_index]

            matrix_q_abs.append(abs(matrix_q[first_index][second_index]))

    q_value: float = max(matrix_q_abs)

    vector_c: vector = [local_vector[index] / local_matrix[index][index] for index in range(count)]

    initial_vector_x: vector = vector_c
    current_vector_x: vector = initial_vector_x.copy()

    condition: bool = True

    while (condition):
        iteration_count += 1
        current_vector_x = initial_vector_x.copy()

        for index in range(count):
            for second_index in range(count):

                if second_index >= first_index:
                    current_vector_x[index] = current_vector_x[index] + matrix_q[first_index][second_index] * \
                                              initial_vector_x[second_index]
                else:
                    current_vector_x[index] = current_vector_x[index] + matrix_q[first_index][second_index] * \
                                              current_vector_x[second_index]

        condition = get_condition_value(current_vector_x, initial_vector_x, q_value, approximation_error)
        initial_vector_x = current_vector_x.copy()

    print_result(iteration_count, current_vector_x)


approximation_error: float = 0.001

matrix_a: matrix = [[6.1, -1.9, 0.4, 0.2], [-1.9, 14.3, 1.8, 1.4], [0.4, 1.8, 12.7, -0.6], [0.2, 1.4, -0.6, 13.1]]
vector_b: vector = [7.1, 10.2, -7.2, 8.6]
matrix_ab: matrix = [[6.1, -1.9, 0.4, 0.2, 7.1], [-1.9, 14.3, 1.8, 1.4, 10.2], [0.4, 1.8, 12.7, -0.6, -7.2],
                     [0.2, 1.4, -0.6, 13.1, 8.6]]

# print("Metoda eliminării lui Gauss: ")
# print("Metoda lui Cholesky: ")
print(f"Metoda iterativă a lui Jacobi cu eroarea {approximation_error}: ")
jacobi_method(matrix_a, vector_b, approximation_error)

print(f"Metoda iterativă a lui Gauss-Seidel cu eroarea {approximation_error}: ")
gauss_seidel_method(matrix_a, vector_b, approximation_error)

#
