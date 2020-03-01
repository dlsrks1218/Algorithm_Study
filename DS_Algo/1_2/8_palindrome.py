def palindrome(s):
    if len(s) < 2:
        return True
    if ' ' in s:
        s = ''.join(s.split(' '))

    half = len(s) // 2

    # print(s[:half], s[half:][::-1])
    if len(s) % 2 == 0:
        if s[:half] == s[half:][::-1]:
            print(s[:half], s[half:][::-1])
            return True
        else:
            return False
    elif len(s) % 2 != 0:
        if s[:half] == s[half+1:][::-1]:
            print(s[:half], s[half+1:][::-1])
            return True
        else:
            return False



def is_palindrome(s):
    # split은 리스트 형태로 리턴
    l = s.split(' ')
    print(type(l))
    # join은 str 형태로 리턴
    s2 = ''.join(l)
    print(type(s2))
    return s2 == s2[::-1]


def is_palindrome2(s):
    s = s.strip()
    print(s)
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return is_palindrome2(s[1:-1])
    else:
        return False
    

if __name__ == '__main__':
    str1 = '다시 합창합시다'
    str2 = ''
    str3 = 'hello'
    
    print(palindrome(str1))
    print(palindrome(str2))
    print(palindrome(str3))
    print()
    print(is_palindrome(str1))
    print(is_palindrome(str2))
    print(is_palindrome(str3))
    print()
    print(is_palindrome2(str1))
    print(is_palindrome2(str2))
    print(is_palindrome2(str3))