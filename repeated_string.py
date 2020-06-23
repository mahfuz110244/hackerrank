# repeated-string https://www.hackerrank.com/challenges/repeated-string
# Complete the repeatedString function below.


def repeatedString(s, n):
    len_s = len(s)
    return s[0:(n % len_s)].count('a') + s.count('a') * int(n / len_s)


if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)
