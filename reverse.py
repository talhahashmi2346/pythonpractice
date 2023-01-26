# Enter your code here. Read input from STDIN. Print output to STDOUT
word = input()
lower, upper, odd, even = [i for i in word if i.islower()], [i for i in word if i.isupper()], [i for i in word if (
            i.isdigit() and int(i) % 2 == 1)], [i for i in word if (i.isdigit() and int(i) % 2 == 0)]
lower.sort(), upper.sort(), odd.sort(), even.sort()
val = lower + upper + odd + even
print(''.join(val))
