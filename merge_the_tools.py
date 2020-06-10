# merge-the-tools https://www.hackerrank.com/challenges/merge-the-tools/
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        sub_string = string[i:i+k:]
        sub_string_list = []
        for i in range(len(sub_string)):
            if sub_string[i] not in sub_string_list:
                sub_string_list.append(sub_string[i])
        print(''.join(sub_string_list))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
