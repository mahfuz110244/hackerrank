if __name__ == '__main__':
    s = input()
    # break down
    for character in s:
        if character.isupper():
            print(True)
            break

    # method 1
    print(next((True for character in s if character.isalnum()), False))
    print(next((True for character in s if character.isalpha()), False))
    print(next((True for character in s if character.isdigit()), False))
    print(next((True for character in s if character.islower()), False))
    print(next((True for character in s if character.isupper()), False))

    # method 2
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
