from mathsom.auxfuncs import reduce_args

def operation_test(x: float) -> float:
    return x**2

def one_arg_function(x: float) -> float:
    return operation_test(x)

def two_arg_function(x: float, y: float) -> float:
    return operation_test(x) + operation_test(y)

reduced_arg_one_arg_function_no_optionals = reduce_args(one_arg_function)
print('Reduced arg one arg function no optionals:')
print(reduced_arg_one_arg_function_no_optionals(7)==49)
print('---------------------------------------------')
reduced_arg_one_arg_function_with_optionals = reduce_args(one_arg_function, [7,2], 0)
print('Reduced arg one arg function with optionals:')
print(reduced_arg_one_arg_function_with_optionals(7)==49)
print('---------------------------------------------')
reduced_arg_two_arg_function = reduce_args(two_arg_function, [7,0], 0)
print('Reduced arg two arg function with second parameter as 0:')
print(reduced_arg_two_arg_function(7)==49)
print('---------------------------------------------')
reduced_arg_two_arg_function_2 = reduce_args(two_arg_function, [7, 2], 0)
print('Reduced arg two arg function with second parameter as constant:')
print(reduced_arg_two_arg_function_2(7)==(49+4))


