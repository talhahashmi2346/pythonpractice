def merge_the_tools(string, k):
    # s_len = len(string)
    # parts = int(s_len / k)
    # pre = 0
    # last = parts
    # total_strings = []
    # for i in range(parts):
    #     mystring = string[pre:last]
    #     newStr = ""
    #     for ch in mystring:
    #         if ch not in newStr:
    #             newStr = newStr + ch
    #     total_strings.append(newStr)
    #     pre = last
    #     last = last + parts
    # for i in total_strings:
    #     print(i)
    start_index = 0
    while start_index < len(string):
        word = string[start_index:start_index + k]
        start_index += k
        lis = []
        for i in word:
            if i not in lis:
                lis.append(i)
        print("".join(lis))

string = 'AABCAAADA'
k = 3
merge_the_tools(string, k)
