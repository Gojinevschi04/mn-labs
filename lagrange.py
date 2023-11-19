from decimal import Decimal

decimal_list = list[Decimal]
epsilon_tolerance: Decimal = Decimal('1E-4')


def print_polynomial(coefficients: decimal_list) -> None:
    degree = len(coefficients) - 1

    print(f"Polynomial of degree {degree}:")
    print(
        f"P(x) = {' + '.join([f'{round(coefficient, 6)} * x^{degree}' for degree, coefficient in enumerate(coefficients)])}")


def interpolate_lagrange(x_data_points: decimal_list, y_function_values: decimal_list) -> decimal_list:
    if len(x_data_points) != len(y_function_values) or len(x_data_points) == 0:
        raise ValueError("Input lists x_data_points and y_function_values must have the same non-zero length.")

    data_points_count: int = len(x_data_points)
    coefficients = [Decimal(0) for _ in range(data_points_count)]

    for first_index in range(data_points_count):

        numerator: Decimal = Decimal(1)
        denominator: Decimal = Decimal(1)

        for second_index in range(data_points_count):

            if second_index != first_index:
                numerator *= (Decimal(0) - x_data_points[second_index])
                denominator *= (x_data_points[first_index] - x_data_points[second_index])

        coefficients[first_index] = y_function_values[first_index] * numerator / denominator

    return coefficients


def compute_divided_difference(x_current: Decimal, x_previous: Decimal, y_current: Decimal,
                               y_previous: Decimal) -> Decimal:
    return (y_previous * x_current - y_current * x_previous) / (x_current - x_previous)


def initialize_interpolation_table(x_values: decimal_list, y_values: decimal_list, interpolation_point: Decimal) -> \
        list[decimal_list]:
    data_points_count: int = len(x_values)
    interpolation_table: list[decimal_list] = [[Decimal(0)] * (data_points_count + 2) for _ in range(data_points_count)]

    for current_point_index in range(data_points_count):
        interpolation_table[current_point_index][0] = Decimal(x_values[current_point_index])
        interpolation_table[current_point_index][1] = Decimal(y_values[current_point_index])
        interpolation_table[current_point_index][2] = Decimal(x_values[current_point_index] - interpolation_point)

    return interpolation_table


def compute_interpolation_result(interpolation_table: list[decimal_list], data_points_count: int) -> Decimal:
    result: Decimal = Decimal(0)

    for current_point_index in range(data_points_count):

        for current_term_index in range(1, data_points_count + 2):

            try:
                x0, x1, y0, y1 = (
                    interpolation_table[current_point_index - current_term_index + 2][2],
                    interpolation_table[current_point_index][2],
                    interpolation_table[current_point_index - 1][current_term_index - 2],
                    interpolation_table[current_point_index][current_term_index - 2],
                )
            except IndexError:
                pass

            if current_term_index > 3:
                y0 = interpolation_table[current_point_index - 1][current_term_index - 1]
                y1 = interpolation_table[current_point_index][current_term_index - 1]

            if interpolation_table[current_point_index][current_term_index] == 0:
                result = compute_divided_difference(x0, x1, y0, y1)
                interpolation_table[current_point_index][current_term_index] = round(result, 4)

            error = abs(
                interpolation_table[current_point_index][current_term_index]
                - interpolation_table[current_point_index - 1][current_term_index - 1]
            )

            if error < epsilon_tolerance:
                break

    return result


def print_interpolation_table(interpolation_table: list[decimal_list]) -> None:
    formatted_table_strings = [
        '|'.join([f'{round(item, 6):10}' for item in row]) + '|' for row in interpolation_table
    ]

    print('\n'.join(formatted_table_strings))


def aitken_interpolation(interpolation_point: Decimal, x_values: decimal_list, y_values: decimal_list) -> Decimal:
    if len(x_values) != len(y_values) or len(x_values) == 0:
        raise ValueError("Input lists x_values and y_values must have the same non-zero length.")

    data_points_count: int = len(x_values)
    interpolation_table: list[decimal_list] = initialize_interpolation_table(x_values, y_values, interpolation_point)

    result: Decimal = compute_interpolation_result(interpolation_table, data_points_count)

    print_interpolation_table(interpolation_table)

    print("\nError:", round(abs(interpolation_table[0][2] - interpolation_table[1][1]), 6))
    print(f'\nf({round(interpolation_point, 5)}) ≈ L({round(interpolation_point, 5)}) = {round(result, 5)}')

    return result


interpolation_point: Decimal = Decimal(-0.532)

x_data_points: decimal_list = [Decimal('-1.432'), Decimal('-0.675'), Decimal('1.439'), Decimal('2.567'),
                               Decimal('3.486'),
                               Decimal('4.910'),
                               Decimal('5.763')]

y_function_values: decimal_list = [Decimal('7.67103'), Decimal('5.45321'), Decimal('3.76129'), Decimal('0.56741'),
                                   Decimal('-1.5630'),
                                   Decimal('0.7684'),
                                   Decimal('2.56793')]

polynomial_degree: int = len(x_data_points)

lagrange_coefficients = interpolate_lagrange(x_data_points, y_function_values)
print_polynomial(lagrange_coefficients)

result: Decimal = Decimal(0.0)

for index in range(len(lagrange_coefficients)):
    result += lagrange_coefficients[index] * interpolation_point ** index

print(f"\nL{polynomial_degree}({round(interpolation_point, 6)}) = {round(result, 6)}")

aitken_interpolation_result = aitken_interpolation(interpolation_point, x_data_points, y_function_values)
