def highFreqLetterCount(word):
    d = dict()
    for ch in word:
        if ch in d.keys():
            break
        d[ch] = 0

    for key in d.keys():
        for ch in word:
            if key == ch:
                d[key] += 1

    return max(d.values())

def solution(word):
    map = {}

    for ch in word:
        if map.get(ch) == None:
            map[ch] = 1
        else:
            map[ch] += 1
        # print(map)
            
    max = -1
    for key in map:
        if map[key] > max:
            max = map[key]
        

    return max

word = 'elegance'
# print(highFreqLetterCount(word))
print(solution(word))