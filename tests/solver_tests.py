from mathsom.solvers import newton_rhapson_solver, bisection_solver
import math


def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def just_x(x):
    return x

def square(x):
    return x**2

def inverse(x):
    return 1/x

def const(x):
    return 2

def sin2args(x, y):
    return math.sin(x)

def cos2args(x, y):
    return math.cos(x)

def just_x2args(x, y):
    return x

def square2args(x, y):
    return x**2

def inverse2args(x, y):
    return 1/x

def const2args(x, y):
    return 2

test_funcs = [just_x, just_x2args, square, square2args]
search_value = 0.95
counter = 0
for func in test_funcs:
    print(f'{func.__name__}')
    if counter%2==0:
        if func.__name__ in ['inverse', 'inverse2args']:
            x_min = 1
        print(f'\tNewton Rhapson solution for search value {search_value} = {newton_rhapson_solver(search_value, func, 2, epsilon=0.0001)}')
        print(f'\tBisection solution for search value {search_value} = {bisection_solver(search_value, func, -10, 10)}')
    else:
        print(f'\tNewton Rhapson solution for search value {search_value} = {newton_rhapson_solver(search_value, func, 2, args=[1, 2], argument_index=0, epsilon=0.0001)}')
        print(f'\tBisection solution for search value {search_value} = {bisection_solver(search_value, func, -10, 10, args=[1, 2], argument_index=0)}')
    print()
    counter += 1
