# https://www.hackerrank.com/challenges/nested-list
mark_sheet = []
score_list = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mark_sheet += [[name, score]]
        score_list += [score]
    second_highest_mark = sorted(list(set(score_list)))[1]
    for name, mark in sorted(mark_sheet):
        if mark == second_highest_mark:
            print(name)
