#  2. swap-case : https://www.hackerrank.com/challenges/swap-case
def swap_case1(input_string):
    input_string = list(input_string)
    toggle_string = ''
    for value in input_string:
        ascii_value = ord(value)
        if 65 <= ascii_value <= 90:
            toggle_string += chr(ascii_value + 32)
        elif 97 <= ascii_value <= 122:
            toggle_string += chr(ascii_value - 32)
        else:
            toggle_string += value
    return toggle_string


def swap_case(input_string):
    return ''.join(value.lower() if value.isupper() else value.upper() for value in input_string)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
