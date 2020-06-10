# the-minion-game https://www.hackerrank.com/challenges/the-minion-game
def minion_game(string):
    # your code goes here
    from itertools import combinations
    # Get all substrings of string
    # Using itertools.combinations()
    # res = [string[x:y] for x, y in combinations(
    #     range(len(string) + 1), r=2)]
    # vowel = 'A', 'E', 'I', 'O', 'U'
    # kevin_sub_count = len([word for word in res if word.startswith(vowel)])
    # stuart_sub_count = len(res) - kevin_sub_count
    # if stuart_sub_count > kevin_sub_count:
    #     print("Stuart", stuart_sub_count)
    # elif kevin_sub_count > stuart_sub_count:
    #     print("Kevin", kevin_sub_count)
    # else:
    #     print("Draw")

    # This is Python. The logic is simple - take all possible substrings, split them into two sets according to
    # starting letter, then sum elements in sets. All possible substrings are string of lenght 1, then strings of
    # length 2 etc. i above is an iterator for that lenght. And then comes a little optimization - if you know the
    # starting letter, you can add all substrings of different length that start with this letter. It will be len(s)
    # - i

    # solution 1:
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    strl = len(s)
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (strl - i)
        else:
            stusc += (strl - i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

    # solution 2:
    vowels = 'AEIOU'
    strl = len(string)
    kevsc = sum(strl - i for i in range(strl) if string[i] in vowels)
    # 1+2+3+....+n=(n*(n+1))/2 That will be the number of all contiguous substrings and then you just need to
    # substract those that Kevin got
    stusc = int(strl * (strl + 1) / 2 - kevsc)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)