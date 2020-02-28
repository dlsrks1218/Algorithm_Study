# 2<=base<=10
def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    return result

def test():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print('test pass')
    
if __name__ == '__main__':
    test()