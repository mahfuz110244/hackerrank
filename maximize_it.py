# maximize-it/ https://www.hackerrank.com/challenges/maximize-it/
# solution explanation help from https://www.thepoorcoder.com/hackerrank-maximize-it-solution/
from itertools import product

if __name__ == '__main__':
    k, m = map(int, input().split())
    n = (list(map(int, input().split()))[1:] for _ in range(k))
    results = map(lambda x: sum(i**2 for i in x) % m, product(*n))
    print(max(results))
