import copy
from decimal import Decimal
from math import exp


def differential_equation(x_value: Decimal, y_value: Decimal) -> Decimal:
    return Decimal(exp(Decimal(-1.2) * x_value)) * (x_value * x_value + Decimal(1.8))


def euler_method(
    y_initial: Decimal, start_x: Decimal, end_x: Decimal, step_size: Decimal
) -> list[Decimal]:
    solution_values: list[Decimal] = [y_initial]
    current_x: Decimal = copy.copy(start_x)
    current_y: Decimal = copy.copy(y_initial)

    while current_x < end_x:
        current_y += step_size * differential_equation(current_x, current_y)
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
        k1: Decimal = step_size * differential_equation(current_x, current_y)
        k2: Decimal = step_size * differential_equation(
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
        k1: Decimal = step_size * differential_equation(current_x, current_y)
        k2: Decimal = step_size * differential_equation(
            current_x + (step_size / 2), current_y + (k1 / 2)
        )
        k3: Decimal = step_size * differential_equation(
            current_x + (step_size / 2), current_y + (k2 / 2)
        )
        k4: Decimal = step_size * differential_equation(
            current_x + step_size, current_y + k3
        )

        current_y += (k1 + 2 * k2 + 2 * k3 + k4) / 6

        solution_values.append(current_y)
        current_x += step_size

    return solution_values
