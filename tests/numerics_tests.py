from mathsom.numerics import differentiate, integrate
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

test_funcs = [sin, sin2args, cos, cos2args, just_x, just_x2args, square, square2args, inverse, inverse2args, const, const2args]
x = math.pi/2
x_min = 0
x_max = math.pi

counter = 0
for func in test_funcs:
    print(f'{func.__name__}')
    if func.__name__ in ['inverse', 'inverse2args']:
        x_min = 1
    else:
        x_min = 0
    if counter%2==0:
        print(f'\tDerivative evaluated at {x} = {differentiate(func, x, step=0.000001)}')
        print(f'\tIntegration between {x_min} and {x_max} = {integrate(func, x_min, x_max)}')
    else:        
        print(f'\tDerivative evaluated at {x} = {differentiate(func, x, args=[1, 2], argument_index=0, step=0.000001)}')        
        print(f'\tIntegration between {x_min} and {x_max} = {integrate(func, x_min, x_max, args=[1, 2], argument_index=0)}')
    print()
    counter += 1
