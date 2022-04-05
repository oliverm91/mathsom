from typing import Union, get_args
import numpy as np
from scipy.interpolate import CubicSpline
from collections.abc import Sequence

def adapt_interpolation_result(x: Union[float, Sequence, np.ndarray], result: Union[float, Sequence, np.ndarray]) -> Union[float, np.ndarray]:
    '''
    Adapts interpolation result to the input x.
    If input is Sequence, result will be adapted to np.ndarray, else result will be a float.
    Parameters
    ----------
    x : Union[float, Sequence, np.ndarray]
        Input x.
    result : Union[float, Sequence, np.ndarray]
        Interpolation result variable to be adapted.
    
    Returns
    -------
    Union[float, np.ndarray]
        Adapted interpolation result variable.'''

    if isinstance(x, get_args(Union[Sequence, np.ndarray])):
        result = np.array(result)
    elif isinstance(result, get_args(Union[Sequence, np.ndarray])):
        result = float(result[0])

    return result

def check_pairs_interpolation(x_input: Union[Sequence, np.ndarray], y_input: Union[Sequence, np.ndarray]) -> None:
    if len(x_input) != len(y_input):
        raise ValueError(f'x_input and y_input must have the same length. x_input: {len(x_input)}, y_input: {len(y_input)}')

def linear_interpolation(x: Union[float, Sequence, np.ndarray], x_input: Union[Sequence, np.ndarray], y_input: Union[Sequence, np.ndarray]) -> Union[float, np.ndarray]:
    '''
    Linear interpolation. interpolates y(x) for a given number of pairs (x, y) received in 2 Sequence or np.ndarray of same length.
    
    Parameters
    ----------
    x : Union[float, Sequence, np.ndarray]
        Value(s) to be interpolated.
    x_input : Union[Sequence, np.ndarray]
        Sequence or np.ndarray of x values.
    y_input : Union[Sequence, np.ndarray]
        Sequence  or np.ndarray of y values.

    Returns
    -------
    Union[float, np.ndarray]
        Interpolated y(x) value(s).
    '''
    check_pairs_interpolation(x_input, y_input)
    result = np.interp(x, x_input, y_input)
    result = adapt_interpolation_result(x, result)
    return result

def loglinear_interpolation(x, x_input, y_input):
    '''
    Log-linear interpolation. interpolates y(x) for a given number of pairs (x, y) received in 2 Sequence or np.ndarray of same length.
    
    Parameters
    ----------
    x : Union[float, Sequence, np.ndarray]
        Value(s) to be interpolated.
    x_input : Union[Sequence, np.ndarray]
        Sequence or np.ndarray of x values.
    y_input : Union[Sequence, np.ndarray]
        Sequence or np.ndarray of y values.
    
    Returns
    -------
    Union[float, np.ndarray]
        Interpolated y(x) value(s).
    '''
    check_pairs_interpolation(x_input, y_input)
    log_y_input = np.log(y_input)
    log_y_result = linear_interpolation(x, x_input, log_y_input)
    result = np.exp(log_y_result)
    result = adapt_interpolation_result(x, result)
    return result
    
def cubic_spline_interpolation(x, x_input, y_input):
    '''
    Cubic spline interpolation. interpolates y(x) for a given number of pairs (x, y) received in 2 Sequence or np.ndarray of same length.
    
    Parameters
    ----------
    x : Union[float, Sequence, np.ndarray]
        Value(s) to be interpolated.
    x_input : Union[Sequence, np.ndarray]
        Sequence or np.ndarray of x values.
    y_input : Union[Sequence, np.ndarray]
        Sequence or np.ndarray of y values.
    
    Returns
    -------
    Union[float, np.ndarray]
        Interpolated y(x) value(s).
    '''
    check_pairs_interpolation(x_input, y_input)
    cs = CubicSpline(x_input, y_input)
    result = cs(x)
    result = adapt_interpolation_result(x, result)
    return result