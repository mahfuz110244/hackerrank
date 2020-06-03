# https://www.hackerrank.com/challenges/designer-door-mat/
if __name__ == '__main__':
    n, m = input().split()  # This must be an odd number
    n = int(n)
    m = int(m)
    c = '.|.'
    width = int((m - 3)/2)
    mid_n = int(n/2)
    # Top
    for i in range(mid_n):
        print((c * i).rjust(width, '-') + c + (c * i).ljust(width, '-'))
    # Middle
    print('WELCOME'.center(m, '-'))

    # Bottom
    for i in range(mid_n):
        print((c * (mid_n - i - 1)).rjust(width, '-') + c + ((c * (mid_n - i - 1)).ljust(width, '-')))
    # # Top Pillars
    # for i in range(thickness + 1):
    #     print((c * thickness).center(thickness * 2, ' ') + (c * thickness).center(thickness * 6, ' '))
    #
    # # Middle Belt
    # for i in range((thickness + 1) // 2):
    #     print((c * thickness * 5).center(thickness * 6, ' '))
    #
    #     # Bottom Pillars
    # for i in range(thickness + 1):
    #     print((c * thickness).center(thickness * 2, ' ') + (c * thickness).center(thickness * 6, ' '))
    #
    #     # Bottom Cone
    # for i in range(thickness):
    #     print(((c * (thickness - i - 1)).rjust(thickness, ' ') + c + (c * (thickness - i - 1)).ljust(
    #         thickness, ' ')).rjust(thickness * 6, ' '))
