def cw3():
    result = [i for i in range(1, 50) if i % 3 != 0]
    return result

if __name__ == '__main__':
    result = cw3()
    print(result)