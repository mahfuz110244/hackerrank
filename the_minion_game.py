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

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)