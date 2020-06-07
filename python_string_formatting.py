# https://www.hackerrank.com/challenges/python-string-formatting/
def print_formatted(number):
    # your code goes here
    # For spacing between the each column, based on the integer limit given.
    w = len(bin(number)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(w, ' '), str(oct(i)[2:]).rjust(w, ' '), str(hex(i)[2:].upper()).rjust(w, ' '),
              str(bin(i)[2:]).rjust(w, ' '))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)