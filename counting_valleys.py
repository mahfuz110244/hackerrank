# counting-valleys https://www.hackerrank.com/challenges/counting-valleys
def countingValleys(n, s):
    v = 0  # of valleys
    lvl = 0  # current level
    for i in range(n):
        if s[i] == 'U':
            lvl += 1
        if s[i] == 'D':
            lvl -= 1

        # if we just came UP to sea level
        if lvl == 0 and s[i] == 'U':
            v += 1
    return v


if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)
