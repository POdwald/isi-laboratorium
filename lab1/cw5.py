from cw4 import cw4

def cw5():
    result = cw4()
    result += [i for i in range(1, 100) if i % 3 == 0 and i % 5 == 0] 
    return result

if __name__ == '__main__':
    result = cw5()
    print(result)