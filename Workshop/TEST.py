def first():
    return "Calling: First function"


def second():
    return "Calling: Second function"


def third():
    return "Calling: Third function"


def default():
    return "Calling: Default function"


var: int = 1

funcs: dict = {
    1: first,
    2: second,
    3: third
}

result = funcs.get(var, default)

print(result())
