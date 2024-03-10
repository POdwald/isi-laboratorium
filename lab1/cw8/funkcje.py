def dodawanie(*args):
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    return sum(args) if len(args) > 1 else args[0]

def odejmowanie(*args):
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    return args[0] - sum(args[1:]) if len(args) > 1 else args[0]

def mnozenie(*args):
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    result = 1
    for num in args:
        result *= num
    
    return result

def dzielenie(*args):
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    result = args[0]
    for num in args[1:]:
        result /= num
    
    return result
