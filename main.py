from math import sqrt
from decimal import Decimal

matrix = list[list[Decimal]]
vector = list[Decimal]


def get_condition_value(
        vector_1: vector, vector_0: vector, q_value: Decimal) -> Decimal:
    count: int = len(vector_1)
    current_vector: vector = [
        Decimal(abs(Decimal(vector_1[index]) - Decimal(vector_0[index])))
        for index in range(count)
    ]
    infinity_matrix_norm: Decimal = Decimal(max(current_vector))

    return Decimal((q_value / (1 - q_value)) * infinity_matrix_norm)


def print_result(iteration_count: int, result_vector: vector) -> None:
    count: int = len(result_vector)

    if iteration_count:
        print(f"\tIteratia: {iteration_count}")

    for index in range(count):
        print(f"x{index + 1} = {result_vector[index]}")


def print_residual_vector(residual_vector: vector) -> None:
    count: int = len(residual_vector)

    print("\tVectorul rezidual:")
    for index in range(count):
        print(f"w{index + 1} = {residual_vector[index]}")


def find_max_pivot(
        extended_matrix: matrix, column_index: int, count: int
) -> tuple[Decimal, int]:
    max_pivot_value: Decimal = abs(extended_matrix[column_index][column_index])
    pivot_row: int = column_index

    for row_index in range(column_index + 1, count):
        current_value = abs(extended_matrix[row_index][column_index])

        if current_value > max_pivot_value:
            max_pivot_value = current_value
            pivot_row = row_index

    return max_pivot_value, pivot_row


def normalize_row(row: list[Decimal], divisor: Decimal) -> list[Decimal]:
    return [Decimal(element / divisor) for element in row]


def eliminate_element(
        target_row: list[Decimal], source_row: list[Decimal], factor: Decimal
) -> list[Decimal]:
    return [target - factor * source for target, source in zip(target_row, source_row)]


def calculate_residual_vector(
        matrix_a: matrix, vector_b: vector, solutions: vector
) -> vector:
    count: int = len(vector_b)
    residual_vector = [Decimal(0) for _ in range(len(solutions))]

    for row_index in range(count):
        for column_index in range(count):
            residual_vector[row_index] += (
                    matrix_a[row_index][column_index] * solutions[column_index]
            )

        residual_vector[row_index] -= vector_b[row_index]

    return residual_vector


def transpose(matrix_l: matrix) -> matrix:
    rows_number, columns_number = len(matrix_l), len(matrix_l[0])

    transposed_matrix: matrix = [
        [matrix_l[row_index][column_index] for row_index in range(rows_number)]
        for column_index in range(columns_number)
    ]

    return transposed_matrix


def cholesky_decomposition(matrix_a: matrix) -> matrix:
    rows_number: int = len(matrix_a)
    matrix_l: matrix = [
        [Decimal(0) for _ in range(rows_number)] for _ in range(rows_number)
    ]

    for row_index in range(rows_number):
        for column_index in range(row_index + 1):
            if row_index == column_index:
                local_sum: Decimal = Decimal(
                    sum(
                        matrix_l[row_index][index] ** 2 for index in range(column_index)
                    )
                )
                matrix_l[row_index][column_index] = Decimal(
                    sqrt(matrix_a[row_index][row_index] - local_sum)
                )
            else:
                local_sum = Decimal(
                    sum(
                        matrix_l[row_index][index] * matrix_l[column_index][index]
                        for index in range(column_index)
                    )
                )

                matrix_l[row_index][column_index] = Decimal(
                    (matrix_a[row_index][column_index] - local_sum)
                    / matrix_l[column_index][column_index]
                )

    return matrix_l


def forward_substitution(matrix_l: matrix, vector_b: vector) -> vector:
    rows_number: int = len(matrix_l)
    vector_y: vector = [Decimal(0) for _ in range(rows_number)]

    for row_index in range(rows_number):
        row_sum: Decimal = Decimal(
            sum(
                matrix_l[row_index][index] * vector_y[index]
                for index in range(row_index)
            )
        )
        vector_y[row_index] = (vector_b[row_index] - row_sum) / matrix_l[row_index][
            row_index
        ]

    return vector_y


def backward_substitution(matrix_l_transpose: matrix, vector_y: vector) -> vector:
    rows_number: int = len(matrix_l_transpose)
    vector_x: vector = [Decimal(0) for _ in range(rows_number)]

    for row_index in range(rows_number - 1, -1, -1):
        diagonal_element: Decimal = matrix_l_transpose[row_index][row_index]
        temp_sum: Decimal = Decimal(
            sum(
                matrix_l_transpose[row_index][column_index] * vector_x[column_index]
                for column_index in range(row_index + 1, rows_number)
            )
        )
        vector_x[row_index] = (vector_y[row_index] - temp_sum) / diagonal_element

    return vector_x


def gauss_method(extended_matrix: matrix, vector_b: vector) -> None:
    rows_count: int = len(extended_matrix)
    columns_count: int = rows_count + 1

    local_matrix = [row.copy() for row in extended_matrix]

    for row_index in range(rows_count):
        divisor: Decimal = Decimal(local_matrix[row_index][row_index])
        local_matrix[row_index] = normalize_row(local_matrix[row_index], divisor)

        for column_index in range(row_index + 1, rows_count):
            factor = local_matrix[column_index][row_index]
            local_matrix[column_index] = eliminate_element(
                local_matrix[column_index], local_matrix[row_index], factor
            )

    solutions = [extended_matrix[index][rows_count] for index in range(rows_count)]

    for row_index in range(rows_count - 1, -1, -1):
        solutions[row_index] = local_matrix[row_index][columns_count - 1]

        for column_index in range(row_index + 1, rows_count):
            solutions[row_index] -= (
                    local_matrix[row_index][column_index] * solutions[column_index]
            )

    residual_vector: vector = calculate_residual_vector(matrix_a, vector_b, solutions)

    print_result(0, solutions)
    print_residual_vector(residual_vector)


def cholesky_method(matrix_a: matrix, vector_b: vector) -> None:
    matrix_l = cholesky_decomposition(matrix_a)
    vector_y = forward_substitution(matrix_l, vector_b)
    vector_x = backward_substitution(transpose(matrix_l), vector_y)

    print_result(0, vector_x)
    residual_vector: vector = calculate_residual_vector(matrix_a, vector_b, vector_x)
    print_residual_vector(residual_vector)


def jacobi_method(
        matrix_a: matrix, vector_b: vector, approximation_error: Decimal
) -> None:
    count: int = len(vector_b)
    iteration_count: int = 0

    matrix_q: matrix = [[Decimal(0) for _ in range(count)] for _ in range(count)]
    matrix_q_abs: vector = [Decimal(0) for _ in range(count ** 2)]

    for row_index in range(count):
        for column_index in range(count):
            if row_index == column_index:
                matrix_q[row_index][column_index] = Decimal(0)

            else:
                matrix_q[row_index][column_index] = (
                        -matrix_a[row_index][column_index] / matrix_a[row_index][row_index]
                )

            matrix_q_abs.append(abs(matrix_q[row_index][column_index]))

    q_value: Decimal = max(matrix_q_abs)

    if q_value < 1:
        print(f"Conditia de convergenta se respecta, q fiind {round(q_value, 5)}.")
    else:
        print(f"Conditia de convergenta nu se respecta, q fiind {round(q_value, 5)}.")
        return

    vector_c: vector = [
        vector_b[index] / matrix_a[index][index] for index in range(count)
    ]

    vector_x_0: vector = vector_c.copy()
    vector_x_k: vector = vector_x_0.copy()

    condition_value: Decimal = Decimal(0.0007)

    while condition_value > approximation_error:
        iteration_count += 1

        for row_index in range(count):
            for column_index in range(count):

                if matrix_q[row_index][column_index]:
                    vector_x_k[row_index] = (
                            matrix_q[row_index][column_index] * vector_x_0[column_index]
                            + vector_c[row_index]
                    )

        condition_value = get_condition_value(
            vector_x_k, vector_x_0, q_value
        )
        vector_x_0 = vector_x_k.copy()
        print_result(iteration_count, vector_x_k)
        print(f"Criteriul de stopare al ciclului: {condition_value}")

    residual_vector: vector = calculate_residual_vector(matrix_a, vector_b, vector_x_k)
    print_residual_vector(residual_vector)


def gauss_seidel_method(
        matrix_a: matrix, vector_b: vector, approximation_error: Decimal
) -> None:
    count: int = len(vector_b)
    iteration_count: int = 0

    matrix_q: matrix = [[Decimal(0) for _ in range(count)] for _ in range(count)]
    matrix_q_abs: vector = [Decimal(0) for _ in range(count ** 2)]

    for row_index in range(count):
        for column_index in range(count):
            if row_index == column_index:
                matrix_q[row_index][column_index] = Decimal(0)

            else:
                matrix_q[row_index][column_index] = (
                        -matrix_a[row_index][column_index] / matrix_a[row_index][row_index]
                )

            matrix_q_abs.append(abs(matrix_q[row_index][column_index]))

    q_value: Decimal = max(matrix_q_abs)

    if q_value < 1:
        print(f"Conditia de convergenta se respecta, q fiind {round(q_value, 5)}.")
    else:
        print(f"Conditia de convergenta nu se respecta, q fiind {round(q_value, 5)}.")
        return

    vector_c: vector = [
        vector_b[index] / matrix_a[index][index] for index in range(count)
    ]

    vector_x_0: vector = vector_c.copy()
    vector_x_k: vector = vector_x_0.copy()

    condition_value: Decimal = Decimal(0.00001)

    while condition_value > approximation_error:
        iteration_count += 1

        for row_index in range(count):
            vector_x_k[row_index] = vector_x_0[row_index]

            for column_index in range(count):
                if matrix_q[row_index][column_index]:
                    if column_index >= row_index:
                        vector_x_k[row_index] = (
                                matrix_q[row_index][column_index] * vector_x_0[column_index]
                                + vector_c[row_index]
                        )
                    else:
                        vector_x_k[row_index] = (
                                matrix_q[row_index][column_index] * vector_x_k[column_index]
                                + vector_c[row_index]
                        )

        condition_value = get_condition_value(
            vector_x_k, vector_x_0, q_value
        )
        vector_x_0 = vector_x_k.copy()
        print_result(iteration_count, vector_x_k)
        print(f"Criteriul de stopare al ciclului: {condition_value}")

    residual_vector: vector = calculate_residual_vector(matrix_a, vector_b, vector_x_k)
    print_residual_vector(residual_vector)


matrix_a: matrix = [
    [Decimal(11.2), Decimal(1.5), Decimal(-1.3), Decimal(0.2)],
    [Decimal(1.5), Decimal(12.1), Decimal(-0.9), Decimal(0.4)],
    [Decimal(-1.3), Decimal(-0.9), Decimal(11.7), Decimal(1.2)],
    [Decimal(0.2), Decimal(0.4), Decimal(1.2), Decimal(13.2)],
]

vector_b: vector = [Decimal(-11.4), Decimal(9.7), Decimal(8.3), Decimal(1.2)]

matrix_ab: matrix = [
    [Decimal(11.2), Decimal(1.5), Decimal(-1.3), Decimal(0.2), Decimal(-11.4)],
    [Decimal(1.5), Decimal(12.1), Decimal(-0.9), Decimal(0.4), Decimal(9.7)],
    [Decimal(-1.3), Decimal(-0.9), Decimal(11.7), Decimal(1.2), Decimal(8.3)],
    [Decimal(0.2), Decimal(0.4), Decimal(1.2), Decimal(13.2), Decimal(1.2)],
]

approximation_error: Decimal = Decimal(0.000001)

# print(f"\n\tMetoda eliminarii lui Gauss: ")
# gauss_method(matrix_ab, vector_b)
#
# print(f"\n\tMetoda Cholesky: ")
# cholesky_method(matrix_a, vector_b)

print(f"\n\tMetoda iterativă a lui Jacobi cu eroarea {round(approximation_error, 6)}: ")
jacobi_method(matrix_a, vector_b, approximation_error)

print(
    f"\n\tMetoda iterativă a lui Gauss-Seidel cu eroarea {round(approximation_error, 6)}: "
)
gauss_seidel_method(matrix_a, vector_b, approximation_error)
