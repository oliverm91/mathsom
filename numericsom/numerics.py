from collections.abc import Sequence, Callable
from auxfuncs import standardize_function
from itertools import accumulate, repeat


def differentiate(func: Callable, arg: float=None, args: Sequence=None, argument_index: int=None, step: float=0.0000001) -> float:
    '''
    Numeric function derivative.
    
    Parameters
    ----------
    func : Callable
        Python objective function to be differentiated.
    arg : float, optional
        Number where function will be differentiated. If function contains many arguments, use func_inputs with partial_argument_index parameters instead. The default is None.
        Example: f'(2) -> arg = 2.
    args : Sequence, optional
        Sequence of inputs of objective funcion. Inputs order in Sequence must be the same as those of the function parameters.
        Example: func(x, y) -> z, args = [x, y]
    argument_index : int, optional
        Index of the parameter to be differentiated within the args Sequence.
        Example: func(x, y) -> z, argument_index = 1 for y.
    step : float, optional
        Step size. The default is 0.000001.
    
    Returns
    -------
    float
        Estimated derivative value.'''
    func = standardize_function(func, args, argument_index)    

    y_fwd_step = func(arg + step)
    y_back_step = func(arg - step)
    slope = (y_fwd_step - y_back_step) / (2.0 * step)
    return slope

def integrate(func: Callable, x_start: float, x_end: float, args: Sequence=None, argument_index: int=None, n_steps: int=10_000):
    '''
    Numeric function integration with Trapezoidal rule.
    
    Parameters
    ----------
    func : Callable
        Python objective function to be integrated.
    x_start : float
        Start value of integration interval.
    x_end : float
        End value of integration interval.
    args : Sequence, optional
        Sequence of inputs of objective funcion. Inputs order in Sequence must be the same as those of the function parameters.
        Example: func(x, y) -> z, args = [x, y]
    argument_index : int, optional
        Index of the parameter to be differentiated within the args Sequence.
        Example: func(x, y) -> z, argument_index = 1 for y.
    n_steps : int, optional
        Number of steps. The default is 10_000.
        
    Returns
    -------
    float
        Estimated integral value.'''
    func = standardize_function(func, args, argument_index)
    step_length = (x_end - x_start) / n_steps
    xs = accumulate(repeat(step_length, n_steps - 2), initial = x_start + step_length)
    area = sum(map(func, xs))
    area = area * 2.0 + func(x_start) + func(x_end)
    return area * step_length / 2.0