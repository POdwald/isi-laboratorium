def cw4():
    result = [i for i in range(1, 50) if i % 3 == 0 and i % 4 == 0] 
    return result

if __name__ == '__main__':
    result = cw4()
    print(result)
    print(len(result))