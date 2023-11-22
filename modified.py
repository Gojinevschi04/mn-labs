import copy
from decimal import Decimal
from math import exp


def print_result(results: list[Decimal]) -> None:
    # print(f"Solutia: {results[-1]}")
    count: int = len(results)

    for index in range(count):
        print(f"Iteratia: {index}")
        print(f"Rezultatul: {round(results[index], 15)}")


def get_differential_expression_value(x_value: Decimal, y_value: Decimal) -> Decimal:
    return Decimal(x_value**2 + Decimal(0.2) * y_value**2)


def euler_method(
    y_initial: Decimal, start_x: Decimal, end_x: Decimal, step_size: Decimal
) -> list[Decimal]:
    solution_values: list[Decimal] = [y_initial]
    current_x: Decimal = copy.copy(start_x)
    current_y: Decimal = copy.copy(y_initial)

    while current_x < end_x:
        current_y += step_size * get_differential_expression_value(current_x, current_y)
        solution_values.append(current_y)
        current_x += step_size

    return solution_values


def modified_euler_method(
    y_initial: Decimal, start_x: Decimal, end_x: Decimal, step_size: Decimal
) -> list[Decimal]:
    solution_values: list[Decimal] = [y_initial]
    current_x: Decimal = copy.copy(start_x)
    current_y: Decimal = copy.copy(y_initial)

    while current_x < end_x:
        k1: Decimal = step_size * get_differential_expression_value(current_x, current_y)
        k2: Decimal = step_size * get_differential_expression_value(
            current_x + (step_size / 2), current_y + (k1 / 2)
        )

        current_y += k2
        solution_values.append(current_y)
        current_x += step_size

    return solution_values


def runge_kutta_method(
    y_initial: Decimal, start_x: Decimal, end_x: Decimal, step_size: Decimal
) -> list[Decimal]:
    solution_values: list[Decimal] = [y_initial]
    current_x: Decimal = copy.copy(start_x)
    current_y: Decimal = copy.copy(y_initial)

    while current_x < end_x:
        k1: Decimal = step_size * get_differential_expression_value(current_x, current_y)
        k2: Decimal = step_size * get_differential_expression_value(
            current_x + (step_size / 2), current_y + (k1 / 2)
        )
        k3: Decimal = step_size * get_differential_expression_value(
            current_x + (step_size / 2), current_y + (k2 / 2)
        )
        k4: Decimal = step_size * get_differential_expression_value(
            current_x + step_size, current_y + k3
        )

        current_y += (k1 + 2 * k2 + 2 * k3 + k4) / 6

        solution_values.append(current_y)
        current_x += step_size

    return solution_values


start_value: Decimal = Decimal(0)
end_value: Decimal = Decimal(1)

initial_y: Decimal = Decimal(0.2)
step_value: Decimal = Decimal(0.05)

print("\nMetoda Euler:")
print_result(euler_method(initial_y, start_value, end_value, step_value))

print("\nMetoda Euler modificat:")
print_result(modified_euler_method(initial_y, start_value, end_value, step_value))

print("\nMetoda Runge – Kutta:")
print_result(runge_kutta_method(initial_y, start_value, end_value, step_value))
