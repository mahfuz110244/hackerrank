# 3. finding - the - percentage: https: // www.hackerrank.com / challenges / finding - the - percentage /

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    # print("{:.2f}".format(sum(marks)/len(marks)))
    print(f'{sum(marks)/len(marks):.2f}')
