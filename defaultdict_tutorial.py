# defaultdict-tutorial https://www.hackerrank.com/challenges/defaultdict-tutorial/

if __name__ == '__main__':
    m, n = map(int, input().split())
    group_a = [input() for i in range(m)]
    group_b = [input() for i in range(n)]
    for i in group_b:
        res_list = [str(j + 1) for j, value in enumerate(group_a) if value == i]
        print(' '.join(res_list) if res_list else '-1')
