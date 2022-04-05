from mathsom.interpolations import interpolate, InterpolationMethod
import numpy as np

print('One X, two lists')
print()
x = 2.5
known_xs = [1,2,3,4,5]
known_ys = [10,20,30,40,50]
print(f'X value: {x}')
print(f'known_xs: {known_xs}')
print(f'known_ys: {known_ys}')

print(f'Linear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LINEAR)}')
print(f'Loglinear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LOGLINEAR)}')
print(f'Cubic spline interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.CUBIC_SPLINE)}')
print('---------------------------------------------')

print('One X, two tuples')
print()
x = 2.5
known_xs = (1,2,3,4,5)
known_ys = (10,20,30,40,50)
print(f'X value: {x}')
print(f'known_xs: {known_xs}')
print(f'known_ys: {known_ys}')

print(f'Linear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LINEAR)}')
print(f'Loglinear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LOGLINEAR)}')
print(f'Cubic spline interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.CUBIC_SPLINE)}')
print('---------------------------------------------')

print('One X, one list one tuple')
print()
x = 2.5
known_xs = [1,2,3,4,5]
known_ys = (10,20,30,40,50)
print(f'X value: {x}')
print(f'known_xs: {known_xs}')
print(f'known_ys: {known_ys}')

print(f'Linear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LINEAR)}')
print(f'Loglinear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LOGLINEAR)}')
print(f'Cubic spline interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.CUBIC_SPLINE)}')
print('---------------------------------------------')

print('One X, two numpy arrays')
print()
x = 2.5
known_xs = np.array([1,2,3,4,5])
known_ys = np.array([10,20,30,40,50])
print(f'X value: {x}')
print(f'known_xs: {known_xs}')
print(f'known_ys: {known_ys}')

print(f'Linear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LINEAR)}')
print(f'Loglinear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LOGLINEAR)}')
print(f'Cubic spline interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.CUBIC_SPLINE)}')
print('---------------------------------------------')

print('List of X, two lists')
print()
x = [2.5, 3.5]
known_xs = [1,2,3,4,5]
known_ys = [10,20,30,40,50]
print(f'X value: {x}')
print(f'known_xs: {known_xs}')
print(f'known_ys: {known_ys}')

print(f'Linear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LINEAR)}')
print(f'Loglinear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LOGLINEAR)}')
print(f'Cubic spline interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.CUBIC_SPLINE)}')
print('---------------------------------------------')

print('Tuple of X, two lists')
print()
x = (2.5, 3.5)
known_xs = [1,2,3,4,5]
known_ys = [10,20,30,40,50]
print(f'X value: {x}')
print(f'known_xs: {known_xs}')
print(f'known_ys: {known_ys}')

print(f'Linear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LINEAR)}')
print(f'Loglinear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LOGLINEAR)}')
print(f'Cubic spline interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.CUBIC_SPLINE)}')
print('---------------------------------------------')

print('Numpy array of X, two lists')
print()
x = np.array([2.5, 3.5])
known_xs = [1,2,3,4,5]
known_ys = [10,20,30,40,50]
print(f'X value: {x}')
print(f'known_xs: {known_xs}')
print(f'known_ys: {known_ys}')

print(f'Linear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LINEAR)}')
print(f'Loglinear interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.LOGLINEAR)}')
print(f'Cubic spline interpolation: {interpolate(x, known_xs, known_ys, InterpolationMethod.CUBIC_SPLINE)}')
print('---------------------------------------------')