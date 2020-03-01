import string
import sys

def count_unique_words():
    words = {}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    for filename in sys.argv[1:]:
        with open(filename) as file:
            for line in file:
                for word in line.lower().split():
                    word = word.atrip(strip)
                    if len(word) > 2:
                        words[word] = words.get(word, 0) + 1

    for word in sorted(words):
        print('{0}: {1}번'.format(word, words[word]))
    
if __name__ == '__main__':
    count_unique_words()