# 2<=base<=10
def convert_dec_to_any_base_rec(number, base):
    convertString = '0123456789ABCDEF'
    if number < base:
        return convertString[number]
    else:
        return convert_dec_to_any_base_rec(number // base, base) + convertString[number % base]

def test():
    number, base = 9, 2
    assert(convert_dec_to_any_base_rec(number, base) == '1001')
    print('test pass')
    
if __name__ == '__main__':
    test()