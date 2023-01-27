def swap_case(s):
    s = list(s)
    s2 = ''
    for i in s:
        if i.isupper():
            s2 += i.lower()
        elif i.islower():
            s2 += i.upper()
        else:
            s2 += i
    return s2


s1 = 'HackerRank.com presents "Pythonist 2".'
print(swap_case(s1))
