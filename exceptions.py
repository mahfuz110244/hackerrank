# exceptions https://www.hackerrank.com/challenges/exceptions/

if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except Exception as e:
            print("Error Code:", e)
