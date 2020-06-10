def solve(s):
    # list = s.split()
    # l[0] = l[0].capitalize()
    # l[-1] = l[-1].capitalize()
    # return ' '.join(l.capitalize() for l in list)
    import string
    # this will capitalize each world of the string and space means don't remove multiple white space
    return string.capwords(s, ' ')


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)