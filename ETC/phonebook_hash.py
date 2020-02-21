size = 10
hash_table = [0 for i in range(size)]

def hash_func(data, size):
    return data%size

def store_data(hash_address, data):
    hash_table[hash_address] = data

def get_data(key):
    return hash_table[hash_func(key, size)]

inp = [119, 97674223, 1195524421]
# inp = [123, 456, 789]
# inp = [12, 123, 1235, 567, 88]

phone_book = dict()
phone_book[119] = '구조대'
phone_book[97674223] = '박준영'
phone_book[1195524421] = '지영석'

for pnum in phone_book:
    address = hash_func(pnum, size)
    store_data(address, phone_book[pnum])

for i in inp:
    print(hash_func(i, size))

# def solution(phone_book):
    






