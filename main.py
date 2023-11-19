# def update_interpolation_table(
#         interpolation_table: List[List[float]],
# ) -> List[List[float]]:
#     number_of_values: int = len(interpolation_table)
#
#     for current_point_index in range(1, number_of_values):
#         print(f"i = {current_point_index}")
#
#         for current_term_index in range(
#                 1, len(interpolation_table[current_point_index])
#         ):
#             print(f"j = {current_point_index}")
#
#             try:
#                 x0, x1, y0, y1 = (
#                     interpolation_table[current_point_index - current_term_index + 2][
#                         2
#                     ],
#                     interpolation_table[current_point_index][2],
#                     interpolation_table[current_point_index - 1][
#                         current_term_index - 2
#                         ],
#                     interpolation_table[current_point_index][current_term_index - 2],
#                 )
#
#                 print(f"x0 = {x0}, y0 = {y0}")
#                 print(f"x1 = {x1}, y1 = {y1}")
#
#             except:
#                 pass
#
#             if current_term_index > 3:
#                 y0 = interpolation_table[current_point_index - 1][
#                     current_term_index - 1
#                     ]
#                 y1 = interpolation_table[current_point_index][current_term_index - 1]
#
#             if interpolation_table[current_point_index][current_term_index] == 0:
#                 result = compute_divided_difference(x0, x1, y0, y1)
#                 interpolation_table[current_point_index][current_term_index] = round(
#                     result, 10
#                 )
#
#                 print(f"Result: {result}\n")
#
#             error = abs(
#                 interpolation_table[current_point_index][current_term_index]
#                 - interpolation_table[current_point_index - 1][current_term_index-1]
#             )
#
#             print(f"Eroarea: {error}\n")
#
#             # if error < epsilon:
#             #     break
#
#     return interpolation_table
#
# import sympy as sp
# from typing import List
# from pprint import pprint
#
#
# def print_polynomial(polynomial_expression: sp.Expr, polynomial_degree: int) -> None:
#     print(f"Polynomial of degree {polynomial_degree}:")
#     print(polynomial_expression)
#
#
# def interpolate_lagrange(
#         x_data_points: List[float], y_function_values: List[float]
# ) -> sp.Expr:
#     if len(x_data_points) != len(y_function_values) or len(x_data_points) == 0:
#         raise ValueError(
#             "Input lists x_data_points and y_function_values must have the same non-zero length."
#         )
#
#     number_of_values: int = len(x_data_points)
#     independent_variable: sp.Symbol = sp.symbols("x")
#     interpolated_polynomial: sp.Expr = sp.sympify(0)
#
#     for current_point_index in range(number_of_values):
#         function_value: sp.Expr = sp.sympify(y_function_values[current_point_index])
#
#         function_value *= compute_lagrange_term(
#             independent_variable, x_data_points, current_point_index
#         )
#
#         interpolated_polynomial += function_value
#
#     simplified_polynomial: sp.Expr = sp.simplify(interpolated_polynomial).evalf()
#
#     return simplified_polynomial
#
#
# def compute_lagrange_term(
#         independent_variable: sp.Symbol,
#         x_data_points: List[float],
#         current_point_index: int,
# ) -> sp.Expr:
#     term: sp.Expr = sp.Integer(1)
#     number_of_values: int = len(x_data_points)
#
#     for index in range(number_of_values):
#
#         if index == current_point_index:
#             continue
#
#         term *= (independent_variable - x_data_points[index]) / (
#                 x_data_points[current_point_index] - x_data_points[index]
#         )
#     return term
#
#
# def compute_divided_difference(x0: float, x1: float, y0: float, y1: float) -> float:
#     return (y0 * x1 - y1 * x0) / (x1 - x0)
#
#
# def build_interpolation_table(
#         interpolation_point: float,
#         x_data_points: List[float],
#         y_function_values: List[float],
# ) -> List[List[float]]:
#     number_of_values: int = len(x_data_points)
#     table_headers: List[str] = ["X Value", "Function Value", "Xi - a"]
#     interpolation_table: List[List[float]] = []
#
#     for current_point_index in range(number_of_values):
#         x_value: float = x_data_points[current_point_index]
#         function_value: float = y_function_values[current_point_index]
#         x_minus_a: float = round(x_value - interpolation_point, 6)
#
#         table_row: List[float] = [x_value, function_value, x_minus_a]
#
#         title: str = "L_"
#
#         for index in range(current_point_index, 0, -1):
#
#             if current_point_index == 0:
#                 continue
#
#             title += f'i-{index}_'
#             table_row.append(0)
#
#         if current_point_index != 0:
#             table_headers.append(title + 'i')
#
#         interpolation_table.append(table_row)
#
#     return interpolation_table
#
#
# def update_interpolation_table(
#         interpolation_table: List[List[float]],
# ) -> List[List[float]]:
#     number_of_values: int = len(interpolation_table)
#
#     for current_point_index in range(1, number_of_values):
#         print(f"i = {current_point_index}")
#
#         for current_term_index in range(
#                 1, len(interpolation_table[current_point_index])
#         ):
#             print(f"j = {current_point_index}")
#
#             try:
#                 x0, x1, y0, y1 = (
#                     interpolation_table[current_point_index - current_term_index + 2][
#                         2
#                     ],
#                     interpolation_table[current_point_index][2],
#                     interpolation_table[current_point_index - 1][
#                         current_term_index - 2
#                         ],
#                     interpolation_table[current_point_index][current_term_index - 2],
#                 )
#
#                 print(f"x0 = {x0}, y0 = {y0}")
#                 print(f"x1 = {x1}, y1 = {y1}")
#
#             except:
#                 pass
#
#             if current_term_index > 3:
#                 y0 = interpolation_table[current_point_index - 1][
#                     current_term_index - 1
#                     ]
#                 y1 = interpolation_table[current_point_index][current_term_index - 1]
#
#             if interpolation_table[current_point_index][current_term_index] == 0:
#                 result = compute_divided_difference(x0, x1, y0, y1)
#                 interpolation_table[current_point_index][current_term_index] = round(
#                     result, 10
#                 )
#
#                 print(f"Result: {result}\n")
#
#             error = abs(
#                 interpolation_table[current_point_index][current_term_index]
#                 - interpolation_table[current_point_index - 1][current_term_index - 1]
#             )
#
#             print(f"Eroarea: {error}\n")
#
#             # if error < epsilon:
#             #     break
#
#     return interpolation_table
#
#
# def print_interpolation_table(interpolation_table: List[List[float]]) -> None:
#     table_headers = ["X Value", "Function Value", "X - a"]
#
#     formatted_table_headers = [
#         header.replace("Lagrange Term_", ",") for header in table_headers
#     ]
#
#     formatted_table = [
#         ["{:14}".format(item) for item in row]
#         for row in [formatted_table_headers] + interpolation_table
#     ]
#
#     formatted_table_strings = ["|".join(row) + "|" for row in formatted_table]
#
#     print("\n".join(formatted_table_strings))
#
#
# def aitken_interpolation(
#         interpolation_point: float,
#         x_data_points: List[float],
#         y_function_values: List[float],
# ) -> float:
#     if len(x_data_points) != len(y_function_values) or len(x_data_points) == 0:
#         raise ValueError(
#             "Input lists x_data_points and y_function_values must have the same non-zero length."
#         )
#
#     interpolation_table: List[List[float]] = build_interpolation_table(
#         interpolation_point, x_data_points, y_function_values
#     )
#     interpolation_table = update_interpolation_table(interpolation_table)
#
#     result: float = interpolation_table[-1][-1]
#
#     print_interpolation_table(interpolation_table)
#
#     # print(f"\nf({interpolation_point}) ≈ L({interpolation_point}) = {result}")
#
#     return result
#
#
# def get_lagrange_polynomials_values(x_data_points: List[float], y_function_values: List[float], alpha: float) -> float:
#     previous_approximation = None
#     number_of_values: int = len(x_data_points)
#     current_approximation: float = 0
#
#     for index in range(1, number_of_values):
#         lagrange_polynomial = interpolate_lagrange(x_data_points[:-index], y_function_values[:-index])
#         current_approximation = lagrange_polynomial.subs('x', alpha)
#
#         # if previous_approximation is not None and abs(current_approximation - previous_approximation) < epsilon:
#         #     break
#
#         previous_approximation = current_approximation
#
#         print(current_approximation)
#
#     return current_approximation
#
#
# epsilon: float = 10 ** -4
#
# interpolation_point: float = -0.532
# x_data_points: List[float] = [-1.432, -0.675, 1.439, 2.567, 3.486, 4.910, 5.763]
#
# y_function_values: List[float] = [
#     7.67103,
#     5.45321,
#     3.76129,
#     0.56741,
#     -1.5630,
#     0.7684,
#     2.56793,
# ]
#
# polynomial_degree: int = len(x_data_points) - 1
#
# interpolated_polynomial: sp.Expr = interpolate_lagrange(
#     x_data_points, y_function_values
# )
# # print_polynomial(interpolated_polynomial, polynomial_degree)
#
# # print(
# #     f"L{polynomial_degree}({interpolation_point}) = {interpolated_polynomial.subs('x', interpolation_point)}"
# # )
#
# # aitken_interpolation_result: float = aitken_interpolation(
# #     interpolation_point, x_data_points, y_function_values
# # )
# get_lagrange_polynomials_values(x_data_points, y_function_values, interpolation_point)
#
# # schema lui aitken