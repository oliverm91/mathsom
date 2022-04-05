from collections.abc import Sequence, Callable

def standardize_function(func: Callable, args: Sequence=None, arg_index: int=None) -> Callable:
        if args is not None and arg_index is None:
            raise ValueError('arg_index must be specified if args is not None')
        if args is None:
            def standardized_function(arg) -> float:
                return func(arg)
        else:
            def standardized_function(arg) -> float:
                args[arg_index] = arg
                return func(*args)

        return standardized_function