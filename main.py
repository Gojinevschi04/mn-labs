from decimal import Decimal

decimal_list = list[Decimal]


def has_unique_values(input_list: decimal_list) -> bool:
    return len(set(input_list)) == len(input_list)


def print_values(x_values: decimal_list, y_values: decimal_list) -> None:
    print("\nInput values are:\n")
    print("X", end="\t")

    for x in x_values:
        print(f"{x:.6f}", end="\t")
    print("\nY", end="\t")

    for y in y_values:
        print(f"{y:.6f}", end="\t")
    print()


def print_lagrange_interpolation_polynomial(intermediate_values: decimal_list):
    degree = len(intermediate_values) - 1
    print("\n1) Lagrange Interpolation Polynomial Ln is:")
    print(f"Ln(x) = {intermediate_values[degree]:.6f}X^{degree}", end=" ")

    current_degree = degree - 1

    for k in range(degree - 1, 0, -1):
        print(f"+{intermediate_values[k]:.6f}X^{current_degree}", end=" ")

        if k == degree - 4:
            print("\n\t", end="")
        current_degree -= 1

    print(f"+{intermediate_values[0]:.6f}")


def calculate_coefficients(x_data: decimal_list) -> decimal_list:
    degree = len(x_data)
    coefficients = [Decimal('0.0') for _ in range(degree)]
    coefficients[0] = Decimal('1')

    for i in range(degree - 1):
        coefficients[i + 1] = coefficients[i]

        for j in range(i, 0, -1):
            coefficients[j] = coefficients[j - 1] - coefficients[j] * x_data[i]
        coefficients[0] = -coefficients[0] * x_data[i]

    return coefficients


def calculate_intermediate_values(x_data: decimal_list, y_data: decimal_list,
                                  coefficients: decimal_list) -> decimal_list:
    degree = len(x_data)
    intermediate_values = [Decimal('0.0') for _ in range(degree + 1)]
    temp_values = [Decimal('0.0') for _ in range(degree + 1)]

    for i in range(degree):
        product = Decimal('1')
        for j in range(degree):
            if i != j:
                product *= (x_data[i] - x_data[j])

        for k in range(degree, -1, -1):
            if k == 0:
                temp_values[k] = Decimal('0.0')
            else:
                temp_values[k] = coefficients[k - 1] + x_data[i] * temp_values[k - 1]

        for k in range(degree + 1):
            intermediate_values[k] += y_data[i] * temp_values[k] / product

    return intermediate_values


def lagrange_interpolation(x_data: decimal_list, y_data: decimal_list, target_x: Decimal) -> Decimal:
    coefficients = calculate_coefficients(x_data)
    intermediate_values = calculate_intermediate_values(x_data, y_data, coefficients)

    degree = len(x_data) - 1
    interpolated_value = intermediate_values[degree]

    for i in range(1, degree + 1):
        interpolated_value = target_x * interpolated_value + intermediate_values[degree - i]

    return interpolated_value


x_values = [Decimal('-1.432'), Decimal('-0.675'), Decimal('1.439'), Decimal('2.567'), Decimal('3.486'),
            Decimal('4.910'),
            Decimal('5.763')]
y_values = [Decimal('7.67103'), Decimal('5.45321'), Decimal('3.76129'), Decimal('0.56741'), Decimal('-1.5630'),
            Decimal('0.7684'),
            Decimal('2.56793')]

target_x_value: Decimal = Decimal(-0.532)

data_length = len(x_values)

result = lagrange_interpolation(x_values, y_values, target_x_value)

print_lagrange_interpolation_polynomial(
    calculate_intermediate_values(x_values, y_values, calculate_coefficients(x_values)))

print(
    f"\n2 The value of the function f(x) at x = {target_x_value:.3f} using the Lagrange interpolation polynomial is: f(x) = {result:.6f}")

print("\nCase where m < n:")
new_length = data_length - 3
reduced_x_values, reduced_y_values = x_values[:new_length], y_values[:new_length]
print_values(reduced_x_values, reduced_y_values)
lagrange_interpolation(reduced_x_values, reduced_y_values, target_x_value)
