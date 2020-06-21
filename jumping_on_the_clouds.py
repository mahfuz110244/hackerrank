# Complete the jumpingOnClouds function below.
# jumping-on-the-clouds https://www.hackerrank.com/challenges/jumping-on-the-clouds/


def jumpingOnClouds(c, n):
    res = 0
    i = 0
    while i < n - 1:
        if i + 2 < n and c[i + 2] == 0:
            i = i + 2
            res += 1
        else:
            i = i + 1
            res += 1
    return res


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, n)
    print(result)
