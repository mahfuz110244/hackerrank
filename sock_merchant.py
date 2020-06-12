# sock-merchant https://www.hackerrank.com/challenges/sock-merchant/
def sockMerchant(n, ar):
    sl = list(set(ar))
    return sum(int(ar.count(i) / 2) for i in sl)


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar[0:n])
    print(result)