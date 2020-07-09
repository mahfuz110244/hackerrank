# py-introduction-to-sets https://www.hackerrank.com/challenges/py-introduction-to-sets


def average(array):
    # your code goes here
    myset = set()
    for i in array:
        myset.add(i)
    return sum(myset) / len(myset)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
