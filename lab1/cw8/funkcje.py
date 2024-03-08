def dodawanie(*args):
    return sum(args) if len(args) > 1 else args[0]

def odejmowanie(*args):
    return args[0] - sum(args[1:]) if len(args) > 1 else args[0]

def mnozenie(*args):
    result = 1
    for num in args:
        result *= num
    
    return result

def dzielenie(*args):
    result = args[0]
    for num in args[1:]:
        result /= num
    
    return result