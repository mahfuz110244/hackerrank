# input https://www.hackerrank.com/challenges/input/

if __name__ == '__main__':
    x, k = input().split()
    x = int(x)
    k = int(k)
    p = input()
    print(eval(p) == k)
