import sympy as sp
from decimal import Decimal


def print_polynomial(polynomial_expression: sp.Expr, polynomial_degree: int) -> None:
    print(f"Polinomul de interpolare Lagrange de gradul {polynomial_degree}:")
    print(polynomial_expression)


def interpolate_lagrange(
    x_data_points: list[Decimal], y_function_values: list[Decimal]
) -> sp.Expr:
    if len(x_data_points) != len(y_function_values) or len(x_data_points) == 0:
        raise ValueError(
            "Input lists x_data_points and y_function_values must have the same non-zero length."
        )

    number_of_values: int = len(x_data_points)
    independent_variable: sp.Symbol = sp.symbols("x")
    interpolated_polynomial: sp.Expr = sp.sympify(0)
    lagrange_term: sp.Expr

    for current_point_index in range(number_of_values):
        function_value: sp.Expr = sp.sympify(y_function_values[current_point_index])

        lagrange_term = compute_lagrange_term(
            independent_variable, x_data_points, current_point_index
        )

        function_value = sp.Mul(function_value, lagrange_term)

        interpolated_polynomial = sp.Add(interpolated_polynomial, function_value)

    simplified_polynomial: sp.Expr = sp.simplify(interpolated_polynomial).evalf()

    return simplified_polynomial


def compute_lagrange_term(
    independent_variable: sp.Symbol,
    x_data_points: list[Decimal],
    current_point_index: int,
) -> sp.Expr:
    term: sp.Expr = sp.Integer(1)
    number_of_values: int = len(x_data_points)

    for index in range(number_of_values):
        if index == current_point_index:
            continue

        numerator: sp.Expr = independent_variable - x_data_points[index]
        denominator: sp.Expr = sp.sympify(
            x_data_points[current_point_index]
        ) - sp.sympify(x_data_points[index])

        term = sp.Mul(term, sp.Pow(denominator, -1) * numerator)

    return term


def get_lagrange_polynomials_values(
    x_data_points: list[Decimal], y_function_values: list[Decimal], alpha: Decimal
) -> Decimal:
    initial_polynom_degree: int = len(x_data_points)
    value: int = len(x_data_points) - 1
    current_approximation: Decimal = Decimal(0)
    previous_approximation: Decimal = Decimal(0)

    while value > 0:
        lagrange_polynomial = interpolate_lagrange(
            x_data_points[:-value], y_function_values[:-value]
        )
        current_approximation = lagrange_polynomial.subs("x", alpha)

        # if abs(current_approximation - previous_approximation) < epsilon:
        #     break
        print(
            f"m = {initial_polynom_degree - value}, Ln{initial_polynom_degree - value} = {current_approximation}"
        )
        value -= 1

        print(f"Eroarea: {abs(current_approximation - previous_approximation)}")
        previous_approximation = current_approximation

    return current_approximation


epsilon: Decimal = Decimal(10**-4)
interpolation_point: Decimal = Decimal(-0.532)

x_data_points: list[Decimal] = [
    Decimal("-1.432"),
    Decimal("-0.675"),
    Decimal("1.439"),
    Decimal("2.567"),
    Decimal("3.486"),
    Decimal("4.910"),
    Decimal("5.763"),
]

y_function_values: list[Decimal] = [
    Decimal("7.67103"),
    Decimal("5.45321"),
    Decimal("3.76129"),
    Decimal("0.56741"),
    Decimal("-1.5630"),
    Decimal("0.7684"),
    Decimal("2.56793"),
]

polynomial_degree: int = len(x_data_points) - 1

interpolated_polynomial: sp.Expr = interpolate_lagrange(
    x_data_points, y_function_values
)

print_polynomial(interpolated_polynomial, polynomial_degree)

interpolated_polynomial_value: Decimal = interpolated_polynomial.subs(
    "x", interpolation_point
)

print(
    f"\nL{polynomial_degree}({round(interpolation_point, 3)}) = {round(interpolated_polynomial_value, 15)}"
)

print("\n Pentru cazul in care m < n:")
get_lagrange_polynomials_values(x_data_points, y_function_values, interpolation_point)
