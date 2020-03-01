def revert(s):
    if s:
        s = s[-1] + revert(s[:-1])
    return s

def revert2(string):
    return string[::-1]

if __name__ == '__main__':
    s1 = '안녕 세상!'
    s2 = revert(s1)
    s3 = revert2(s1)
    print(s2, s3)