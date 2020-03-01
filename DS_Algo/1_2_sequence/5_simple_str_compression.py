def str_compression(s):
    count, last = 1, ''
    list_aux = []
    for i, c in enumerate(s):
        if last == c:
            count += 1
        else:
            if i != 0:
                list_aux.append(str(count))
                print(list_aux)
            list_aux.append(c)
            count = 1
            last = c
            print(list_aux)

    list_aux.append(str(count))
    print('result :', list_aux)
    return ''.join(list_aux)

if __name__ == '__main__':
    result = str_compression('aaabbcbbbcccaaa')
    print(result)