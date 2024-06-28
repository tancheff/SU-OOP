def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


closure_example = outer_function(10)
print(closure_example(5))  # Output: 15
print(closure_example(20))  # Output: 30
