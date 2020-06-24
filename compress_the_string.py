# compress-the-string https://www.hackerrank.com/challenges/compress-the-string

from itertools import groupby

print(*[(len(list(v)), int(k)) for k, v in groupby(input())])
