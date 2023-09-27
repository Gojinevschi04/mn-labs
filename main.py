from math import sin, cos, exp


def get_expression_value_a(value: float) -> float:
    return exp(-value) * sin(value) + 1


def get_expression_value_b(value: float) -> float:
    return value ** 3 + 9 * value - 3


def get_expression_derivative_value_a(value: float) -> float:
    return exp(-value) * (cos(value) - sin(value))


def get_expression_derivative_value_b(value: float) -> float:
    return 3 * value ** 2 + 9


def get_expression_fi_value_a(value: float) -> float:
    return exp(value) + sin(value) + value


def get_expression_fi_value_b(value: float) -> float:
    return 3 / (value ** 2 + 9)


def print_result(iteration_count: int, result: float, difference: float) -> None:
    print(f"Iteratia: {iteration_count}")
    print(f"Rezultatul: {result}")
    print(f"Diferenta: {difference}")


def interval_halving_method_a(start: float, end: float, approximation: float) -> None:
    iteration_count: int = 1

    while end - start > approximation:
        middle: float = (start + end) / 2
        function_start_value: float = get_expression_value_a(start)
        function_middle_value: float = get_expression_value_a(middle)

        if function_start_value * function_middle_value < 0:
            end = middle
        else:
            start = middle

        print(f"Iteratia: {iteration_count}")
        print(f"x = ( {start} , {end} )")
        iteration_count += 1


def interval_halving_method_b(start: float, end: float, approximation: float) -> None:
    iteration_count: int = 1

    while end - start > approximation:

        middle: float = (start + end) / 2
        function_start_value: float = get_expression_value_b(start)
        function_middle_value: float = get_expression_value_b(middle)

        if function_start_value * function_middle_value < 0:
            end = middle
        else:
            start = middle

        print(f"Iteratia: {iteration_count}")
        print(f"x = ( {start} , {end} )")
        iteration_count += 1


def method_of_successive_approximations_a(start: float, end: float, approximation: float) -> None:
    iteration_count: int = 0

    while abs(start - end) > approximation:
        end = get_expression_fi_value_a(start)
        print_result(iteration_count, end, abs(start - end))

        iteration_count += 1
        start = get_expression_fi_value_b(end)

        print_result(iteration_count, start, abs(start - end))
        iteration_count += 1


def method_of_successive_approximations_b(start: float, end: float, approximation: float) -> None:
    iteration_count: int = 0

    while abs(start - end) > approximation:
        end = get_expression_fi_value_b(start)
        print_result(iteration_count, end, abs(start - end))

        iteration_count += 1
        start = get_expression_fi_value_b(end)

        print_result(iteration_count, start, abs(start - end))
        iteration_count += 1


def tangent_method_a(initial_value_x: float, approximation: float) -> None:
    iteration_count: int = 0

    current_x: float = initial_value_x - get_expression_value_a(initial_value_x) / get_expression_derivative_value_a(
        initial_value_x)
    print_result(iteration_count + 1, current_x, abs(current_x - initial_value_x))

    while abs(initial_value_x - current_x) > approximation:
        initial_value_x = current_x - get_expression_value_a(current_x) / get_expression_derivative_value_a(current_x)
        iteration_count += 1

        print_result(iteration_count + 1, initial_value_x, abs(current_x - initial_value_x))
        current_x = initial_value_x - get_expression_value_a(initial_value_x) / get_expression_derivative_value_a(
            initial_value_x)
        iteration_count += 1

        print_result(iteration_count + 1, current_x, abs(current_x - initial_value_x))


def tangent_method_b(initial_value_x: float, approximation: float) -> None:
    iteration_count: int = 0

    current_x: float = initial_value_x - get_expression_value_b(initial_value_x) / get_expression_derivative_value_b(
        initial_value_x)
    print_result(iteration_count + 1, current_x, abs(current_x - initial_value_x))

    while abs(initial_value_x - current_x) > approximation:
        initial_value_x = current_x - get_expression_value_b(current_x) / get_expression_derivative_value_b(current_x)
        iteration_count += 1

        print_result(iteration_count + 1, initial_value_x, abs(current_x - initial_value_x))
        current_x = initial_value_x - get_expression_value_b(initial_value_x) / get_expression_derivative_value_b(
            initial_value_x)
        iteration_count += 1

        print_result(iteration_count + 1, current_x, abs(current_x - initial_value_x))


def secant_method_a(start: float, end: float, approximation: float) -> None:
    iteration_count: int = 0

    while abs(start - end) > approximation:

        x_value: float = start - get_expression_value_a(start) * (end - start) / (
                get_expression_value_a(end) - get_expression_value_a(start))

        function_start_value: float = get_expression_value_a(start)
        function_end_value: float = get_expression_value_a(end)

        if function_start_value * function_end_value < 0:
            end = x_value
        else:
            start = x_value

        print_result(iteration_count + 1, x_value, abs(start - end))
        iteration_count += 1


def secant_method_b(start: float, end: float, approximation: float) -> None:
    iteration_count: int = 0

    while abs(start - end) > approximation:

        x_value: float = start - get_expression_value_b(start) * (end - start) / (
                get_expression_value_b(end) - get_expression_value_b(start))

        function_start_value: float = get_expression_value_b(start)
        function_end_value: float = get_expression_value_b(end)

        if function_start_value * function_end_value < 0:
            end = x_value
        else:
            start = x_value

        print_result(iteration_count + 1, x_value, abs(start - end))
        iteration_count += 1


start_a: float = float(input("Introduceti intervalul de calcul:\na = "))
end_a: float = float(input("b = "))

start_b: float = float(input("Introduceti intervalul de calcul:\na = "))
end_b: float = float(input("b = "))

approximation_value: float = float(input("Introduceti aproximarea:\nepsilon = "))
