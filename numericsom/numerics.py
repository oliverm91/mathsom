import numpy as np
from scipy.interpolate import CubicSpline
from collections.abc import Iterable

def newton_rhapson_solver(objective_value: float, func, initial_guess: list, argument_index: int, epsilon: float=0.0000001, finite_difference_step: float=0.000001) -> float:
    '''
    Generalized Newton Rhapson Solver for any Python function that returns a float number.

    Parameters
    ----------
    objective_value : float
        Solution value to obtain from objective function.
    func : TYPE
        Python objective function to be solved.
    initial_guess : list
        List of inputs of objective funcion. Inputs order in list must be the same as those of the function parameters.
    argument_index : int
        Index of the parameter to be solved within the initial_guess List.
    epsilon : float, optional
        Minimum step value for solution. The default is 0.0000001.
    finite_difference_step : float, optional
        Step size for numeric solution of the partial derivative respect to the variable to be guessed. The default is 0.000001.

    Returns
    -------
    float
        Estimated solution value.

    '''
    step = 1_000.0 * epsilon
    solution = initial_guess.copy()
    while abs(step) > epsilon:
        estimated_value = func(*solution)
        slope = single_variable_finite_difference(func, solution, argument_index, finite_difference_step)
        step = (estimated_value - objective_value) / slope
        solution[argument_index] -= step
    
    solution_value = solution[argument_index]
    return solution_value

def single_variable_finite_difference(func, args: list, partial_argument_index: int, step: float=0.0000001) -> float:
    '''
    Calculates the partial derivative value of a generalized python function respect to a single numerical variable.

    Parameters
    ----------
    func : TYPE
        Python objective function to be differenciated.
    args : list
        List of inputs of objective funcion. Inputs order in list must be the same as those of the function parameters..
    partial_argument_index : int
        Index of the parameter to be differenciated within the initial_guess List..
    step : float
        Step size for numeric solution of the partial derivative to the variable to be guessed.

    Returns
    -------
    float
        Estimated slope value.

    '''
    
    fwd_step_args = args.copy()
    fwd_step_args[partial_argument_index] += step
    back_step_args = args.copy()
    back_step_args[partial_argument_index] -= step
    y_fwd_step = func(*fwd_step_args)
    y_back_step = func(*back_step_args)
    slope = (y_fwd_step - y_back_step) / (2.0 * step)
    return slope

def linear_interpolation(x, x_input, y_input):
    result = np.interp(x, x_input, y_input)
    return result if isinstance(x, Iterable) else result[0]

def loglinear_interpolation(x, x_input, y_input):
    log_y_input = np.log(y_input)
    log_y_result = linear_interpolation(x, x_input, log_y_input)
    result = np.exp(log_y_result)
    return result if isinstance(x, Iterable) else result[0]
    
def cubic_spline_interpolation(x, x_input, y_input):
    cs = CubicSpline(x_input, y_input)
    result = cs(x)
    return result if isinstance(x, Iterable) else result[0]