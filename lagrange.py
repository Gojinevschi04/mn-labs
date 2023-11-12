import sympy as sp
from typing import List

epsilon_tolerance: float = 10 ** -4


def print_polynomial(polynomial_expression: sp.Expr, polynomial_degree: int) -> None:
    print(f"Polynomial of degree {polynomial_degree}:")
    print(sp.pretty(polynomial_expression))


def interpolate_lagrange(x_data_points: List[float], y_function_values: List[float]) -> sp.Expr:
    if len(x_data_points) != len(y_function_values) or len(x_data_points) == 0:
        raise ValueError("Input lists x_data_points and y_function_values must have the same non-zero length.")

    independent_variable: sp.Symbol = sp.symbols('x')

    interpolated_polynomial: sp.Expr = sp.sympify(0)
    data_points_count: int = len(x_data_points)

    for i in range(data_points_count):
        function_value: sp.Expr = sp.sympify(y_function_values[i])
        for j in range(data_points_count):
            if j == i:
                continue
            function_value *= (independent_variable - x_data_points[j]) / (x_data_points[i] - x_data_points[j])
        interpolated_polynomial += function_value

    simplified_polynomial: sp.Expr = sp.simplify(interpolated_polynomial).evalf()

    return simplified_polynomial


def compute_divided_difference(x0: float, x1: float, y0: float, y1: float) -> float:
    return (y0 * x1 - y1 * x0) / (x1 - x0)


def aitken_interpolation(interpolation_point: float, x_data_points: List[float],
                         y_function_values: List[float]) -> float:
    if len(x_data_points) != len(y_function_values) or len(x_data_points) == 0:
        raise ValueError("Input lists x_data_points and y_function_values must have the same non-zero length.")

    interpolation_table_headers: List[str] = ["X Value", "Function Value", "X - a"]
    interpolation_table: List[List[float]] = []

    for current_point_index in range(len(x_data_points)):
        x_value: float = x_data_points[current_point_index]
        function_value: float = y_function_values[current_point_index]
        x_minus_a: float = round(x_value - interpolation_point, 5)
        table_row: List[float] = [x_value, function_value, x_minus_a]

        term_title: str = "Lagrange Term_"
        for current_term_index in range(current_point_index, 0, -1):
            if current_point_index == 0:
                continue
            term_title += f'i-{current_term_index}_'
            table_row.append(0)

        if current_point_index != 0:
            interpolation_table_headers.append(term_title + 'i')

        interpolation_table.append(table_row)

    result: float = 0
    error: float = 0

    for current_point_index in range(len(interpolation_table)):
        for current_term_index in range(1, len(interpolation_table[current_point_index])):

            try:
                x0, x1, y0, y1 = interpolation_table[current_point_index - current_term_index + 2][2], \
                    interpolation_table[current_point_index][2], interpolation_table[current_point_index - 1][
                    current_term_index - 2], interpolation_table[current_point_index][current_term_index - 2]
            except:

                pass
            if current_term_index > 3:
                y0 = interpolation_table[current_point_index - 1][current_term_index - 1]
                y1 = interpolation_table[current_point_index][current_term_index - 1]

            if interpolation_table[current_point_index][current_term_index] == 0:
                result = compute_divided_difference(x0, x1, y0, y1)
                interpolation_table[current_point_index][current_term_index] = round(result, 4)

            error = abs(interpolation_table[current_point_index][current_term_index] -
                        interpolation_table[current_point_index - 1][current_term_index - 1])

            if error < epsilon_tolerance:
                break

    formatted_table_headers = [header.replace("Lagrange Term_", ",") for header in interpolation_table_headers]
    formatted_table = [['{:10}'.format(item) for item in row] for row in
                       [formatted_table_headers] + interpolation_table]
    formatted_table_strings = ['|'.join(row) + '|' for row in formatted_table]
    print('\n'.join(formatted_table_strings))

    print("Error:", error)
    print(f'f({interpolation_point}) ≈ L({interpolation_point}) = {result}')

    return result


# Input values
polynomial_degree: int = 6
interpolation_point: float = 0.204
x_data_points: List[float] = [0.104, 0.205, 0.310, 0.401, 0.507, 0.618, 0.721]
y_function_values: List[float] = [4.96713, 6.811347, 8.76712, 10.16147, 9.12347, 7.26493, 5.37149]

# Perform Lagrange interpolation and Aitken's interpolation
interpolated_polynomial: sp.Expr = interpolate_lagrange(x_data_points, y_function_values)
print_polynomial(interpolated_polynomial, polynomial_degree)

print(f"L{polynomial_degree}({interpolation_point}) = {interpolated_polynomial.subs('x', interpolation_point)}")
print("For a =", interpolation_point, "Ln(", interpolation_point, ") =",
      interpolated_polynomial.subs('x', interpolation_point), polynomial_degree)

aitken_interpolation_result: float = aitken_interpolation(interpolation_point, x_data_points, y_function_values)
