# word-order https://www.hackerrank.com/challenges/word-order/

# My solution
if __name__ == '__main__':
    n = int(input())
    dw = {}
    for _ in range(n):
        word = input()
        if word not in dw.keys():
            dw[word] = 1
        else:
            dw[word] += 1
    print(len(dw.keys()))
    print(*dw.values())

# another solution
from collections import OrderedDict

words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1

print(len(words))
print(*words.values())
