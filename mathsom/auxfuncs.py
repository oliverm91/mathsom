from collections.abc import Sequence, Callable

def reduce_args(func: Callable, args: Sequence=None, arg_index: int=None) -> Callable:
    '''
    Returns a function that has been reduced to a single argument.
    
    Parameters
    ----------
    func : Callable
        Python function to be reduced.
    args : Sequence, optional
        Sequence of function. Inputs order in Sequence must be the same as those of the function parameters.
        Example: func(x, y) -> z, args = [x, y]
    arg_index : int, optional
        Index of the parameter to be kept after reducing inputs.
        Example: func(x, y) -> z, arg_index = 1 for y.
    
    Returns
    -------
    Callable
        Function with one argument f(x).'''
    if args is not None and arg_index is None:
        raise ValueError('arg_index must be specified if args is not None')
    if args is None:
        def reduced_func(arg) -> float:
            return func(arg)
    else:
        def reduced_func(arg) -> float:
            args[arg_index] = arg
            return func(*args)

    return reduced_func