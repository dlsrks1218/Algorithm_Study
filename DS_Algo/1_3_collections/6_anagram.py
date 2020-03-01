# anagram : 문장 또는 단어의 철자 순서를 바꾸는 놀이

def anagram(s):
    res = 0
    for ch in s:
        if ch == ' ':
            continue
        res += ord(ch)
    return res


def find_anagram(word1, word2):
    return anagram(word1) == anagram(word2)


def test_anagram():
    w1 = 'buffy'
    w2 = 'bffyu'
    w3 = 'bhhya'
    assert(find_anagram(w1, w2) is True)
    assert(find_anagram(w1, w3) is False)
    print('test pass')


if __name__ == '__main__':
    test_anagram()
