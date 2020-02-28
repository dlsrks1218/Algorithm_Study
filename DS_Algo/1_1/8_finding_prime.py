import math
import random


def finding_prime(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


def finding_prime_sqrt(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, int(math.sqrt(num)) + 1):
        if number % x == 0:
            return False
    return True


def test():
    num1 = 17
    num2 = 20

    assert(finding_prime(num1) == True)
    assert(finding_prime(num2) == False)
    assert(finding_prime_sqrt(num1) == True)
    assert(finding_prime_sqrt(num2) == False)

    print('test pass')

if __name__ == '__main__':
    test()