import sympy as sp
from typing import List


def print_polynomial(polynomial_expression: sp.Expr, polynomial_degree: int) -> None:
    print(f"Polynomial of degree {polynomial_degree}:")
    print(sp.pretty(polynomial_expression))


def interpolate_lagrange(
        x_data_points: List[float], y_function_values: List[float]
) -> sp.Expr:
    if len(x_data_points) != len(y_function_values) or len(x_data_points) == 0:
        raise ValueError(
            "Input lists x_data_points and y_function_values must have the same non-zero length."
        )

    independent_variable: sp.Symbol = sp.symbols("x")

    interpolated_polynomial: sp.Expr = sp.sympify(0)

    for current_point_index in range(len(x_data_points)):
        function_value: sp.Expr = sp.sympify(y_function_values[current_point_index])
        function_value *= compute_lagrange_term(
            independent_variable, x_data_points, current_point_index
        )
        interpolated_polynomial += function_value

    simplified_polynomial: sp.Expr = sp.simplify(interpolated_polynomial).evalf()

    return simplified_polynomial


def compute_lagrange_term(
        independent_variable: sp.Symbol,
        x_data_points: List[float],
        current_point_index: int,
) -> sp.Expr:
    term: sp.Expr = sp.Integer(1)
    for j in range(len(x_data_points)):
        if j == current_point_index:
            continue
        term *= (independent_variable - x_data_points[j]) / (
                x_data_points[current_point_index] - x_data_points[j]
        )
    return term


def compute_divided_difference(x0: float, x1: float, y0: float, y1: float) -> float:
    return (y0 * x1 - y1 * x0) / (x1 - x0)


def build_interpolation_table(
        interpolation_point: float,
        x_data_points: List[float],
        y_function_values: List[float],
) -> List[List[float]]:
    table_headers: List[str] = ["X Value", "Function Value", "Xi - a"]
    interpolation_table: List[List[float]] = []

    for current_point_index in range(len(x_data_points)):
        x_value: float = x_data_points[current_point_index]
        function_value: float = y_function_values[current_point_index]
        x_minus_a: float = round(x_value - interpolation_point, 5)
        table_row: List[float] = [x_value, function_value, x_minus_a]
        interpolation_table.append(table_row)

    return interpolation_table


def update_interpolation_table(
        interpolation_table: List[List[float]],
) -> List[List[float]]:
    for current_point_index in range(len(interpolation_table)):
        for current_term_index in range(
                1, len(interpolation_table[current_point_index])
        ):
            try:
                x0, x1, y0, y1 = (
                    interpolation_table[current_point_index - current_term_index + 2][
                        2
                    ],
                    interpolation_table[current_point_index][2],
                    interpolation_table[current_point_index - 1][
                        current_term_index - 2
                        ],
                    interpolation_table[current_point_index][current_term_index - 2],
                )
            except:
                pass
            if current_term_index > 3:
                y0 = interpolation_table[current_point_index - 1][
                    current_term_index - 1
                    ]
                y1 = interpolation_table[current_point_index][current_term_index - 1]
            if interpolation_table[current_point_index][current_term_index] == 0:
                result = compute_divided_difference(x0, x1, y0, y1)
                interpolation_table[current_point_index][current_term_index] = round(
                    result, 4
                )

            error = abs(
                interpolation_table[current_point_index][current_term_index]
                - interpolation_table[current_point_index - 1][current_term_index - 1]
            )

            if error < epsilon:
                break

    return interpolation_table


def print_interpolation_table(interpolation_table: List[List[float]]) -> None:
    table_headers = ["X Value", "Function Value", "X - a"]
    formatted_table_headers = [
        header.replace("Lagrange Term_", ",") for header in table_headers
    ]
    formatted_table = [
        ["{:10}".format(item) for item in row]
        for row in [formatted_table_headers] + interpolation_table
    ]
    formatted_table_strings = ["|".join(row) + "|" for row in formatted_table]
    print("\n".join(formatted_table_strings))


def aitken_interpolation(
        interpolation_point: float,
        x_data_points: List[float],
        y_function_values: List[float],
) -> float:
    if len(x_data_points) != len(y_function_values) or len(x_data_points) == 0:
        raise ValueError(
            "Input lists x_data_points and y_function_values must have the same non-zero length."
        )

    interpolation_table: List[List[float]] = build_interpolation_table(
        interpolation_point, x_data_points, y_function_values
    )
    interpolation_table = update_interpolation_table(interpolation_table)

    result: float = interpolation_table[-1][-1]

    print_interpolation_table(interpolation_table)

    print(f"f({interpolation_point}) ≈ L({interpolation_point}) = {result}")

    return result


epsilon: float = 10 ** -4

interpolation_point: float = 0.204
x_data_points: List[float] = [-1.432, -0.675, 1.439, 2.567, 3.486, 4.910, 5.763]

y_function_values: List[float] = [
    7.67103,
    5.45321,
    3.76129,
    0.56741,
    -1.5630,
    0.7684,
    2.56793,
]

polynomial_degree: int = len(x_data_points)

interpolated_polynomial: sp.Expr = interpolate_lagrange(
    x_data_points, y_function_values
)
print_polynomial(interpolated_polynomial, polynomial_degree)

print(
    f"L{polynomial_degree}({interpolation_point}) = {interpolated_polynomial.subs('x', interpolation_point)}"
)
print(
    "For a =",
    interpolation_point,
    "Ln(",
    interpolation_point,
    ") =",
    interpolated_polynomial.subs("x", interpolation_point),
    polynomial_degree,
)

aitken_interpolation_result: float = aitken_interpolation(
    interpolation_point, x_data_points, y_function_values
)
