from collections.abc import Sequence, Callable
from .numerics import differentiate
from .auxfuncs import reduce_args


def newton_rhapson_solver(objective_value: float, func: Callable, initial_guess: float, args: Sequence=None, argument_index: int=None, max_steps: int=100, epsilon: float=0.0000001, differentiation_step=0.0000001, verbose_step=True, retry=True) -> float:
    '''
    Newton Rhapson Solver for any Python function that returns a float number.
    
    Parameters
    ----------
    objective_value: float
        Solution value to be achieved.
    func: Callable
        Python objective function to be solved.
    initial_guess: float
        Initial guess solution.
    args: Sequence, optional
        Sequence of inputs of objective function. If function has other arguments like f(x,y) -> z then args: [x, y].
    argument_index: int, optional
        Index of the parameter to be differentiated within the args Sequence.
        Example: func(x, y) -> z, argument_index = 1 for y.
    max_steps: int, optional
        Maximum number of iterations. Default is 100.
    epsilon: float, optional
        Stoping criteria: step < epsilon. Default is 0.0000001.
    differentiation_step: float, optional
        Step size for numerical differentiation. Default is 0.0000001.
    verbose_step: bool, optional
        Prints error when slope is 0. Default is True.
    retry: bool, optional
        Retries one time if slope is 0 increasing differentiation_step in *10. Default is True.
        
    Returns
    -------
    float
        Estimated solution value.
    '''
    func = reduce_args(func, args, argument_index)

    step = 1_000.0 * epsilon
    solution = initial_guess
    steps = 0
    try:
        while abs(step) > epsilon or steps > max_steps:
            estimated_value = func(solution)
            slope = differentiate(func, solution, argument_index)
            step = (estimated_value - objective_value) / slope
            solution -= step
            steps += 1
        if abs(step) > epsilon:
            raise ValueError(f'Maximum number of steps reached, but convergence criteria not met. Last step: {step} > epsilon: {epsilon}.')
        return solution
        
    except ZeroDivisionError as zde:
        if verbose_step:
            print('ZeroDivisionError: slope is zero')
        if retry:
            if verbose_step:
                print('Retrying...')
            solution = newton_rhapson_solver(objective_value, func, initial_guess, args, argument_index, max_steps, epsilon * 10, differentiation_step * 10, verbose_step, retry=False)
            return solution
        else:
            raise zde

def bisection_solver(objective_value: float, func: Callable, lower_bound: float, higher_bound: float, args: Sequence=None, argument_index: int=None, epsilon: float=0.0000001, max_iters: int=100) -> float:
    '''
    Bisection Solver for any Python function that returns a float number.
    
    Parameters
    ----------
    objective_value: float
        Solution value to be achieved.
    func: Callable
        Python objective function to be solved.
    lower_bound: float
        Lower bound solution of the interval to be searched.
    higher_bound: float
        Higher bound solution of the interval to be searched.
    epsilon: float, optional
        Stoping criteria: (f(guess)-objective_value)*(f(updated_lower_bound)-objective_value) < epsilon. Default is 0.0000001.
    max_iters: int, optional
        Maximum number of iterations. Default is 100.
    func_inputs: Sequence, optional
        Sequence of inputs of objective function. Inputs order in Sequence must be the same as those of the function parameters.
        Example: func(x, y) -> z, func_inputs = [x, y]
    argument_index: int, optional
        Index of the parameter to be solved within the initial_guess Sequence.
        Example: func(x, y) -> z, argument_index = 1 for y.

    Returns
    -------
    float
        Estimated solution value.
    '''
    func = reduce_args(func, args, argument_index)
    def objective_function(x):
        return func(x) - objective_value
    
    guess = (lower_bound + higher_bound) / 2.0
    iters = 0
    while iters < max_iters:
        f_guess = objective_function(guess)
        f_lower_bound = objective_function(lower_bound)
        aux = f_guess * f_lower_bound
        if abs(aux) < epsilon:
            return guess
        iters += 1
        if aux > 0:
            lower_bound = guess
        elif aux < 0:
            higher_bound = guess
        guess = (lower_bound + higher_bound) / 2.0

    if abs(aux) > epsilon:
        raise ValueError(f'Maximum number of iterations reached, but convergence criteria not met. f_low*f_guess: {aux} > epsilon: {epsilon}.')
    
    return guess