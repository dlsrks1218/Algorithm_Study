def finding_gcd(a, b):
    # while not b == 0:
    # while not b == 0:
    while b != 0:
        result = b
        a, b = b, a % b
        # print(a, b)
    return result

def test():
    num1 = 21
    num2 = 12
    assert(finding_gcd(num1, num2) == 3)
    print('test pass')

if __name__ == '__main__':
    test()