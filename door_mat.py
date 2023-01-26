# Size: 7 x 21
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
#
# Size: 11 x 33
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME-------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------
N ,M =map(int,input().split())
dash = '-'
dot = '.'
vert_bar = '|'
n = 3
D = int((M - n) / 2)
count = 1
for i in range(0, N):
    if i == int((N - 1) / 2):
        wel = int((M - 7)/2)
        for x in range(wel):
            print(dash, end='')
        print('WELCOME', end='')
        for x in range(wel):
            print(dash, end='')
        print()
    elif i <= int((N-1) / 2):
        for k in range(0, D):
            print(dash, end='')
        ans = int(n/3)
        for l in range(0, ans):
            print(dot, end='')
            print(vert_bar, end='')
            print(dot, end='')
        for m in range(0, D):
            print(dash, end='')
        print()
        count = count + 2
        n = 3 * count
        D = D - 3
    elif i < N:
        count = count - 2
        n = 3 * count
        D = D + 3
        for k1 in range(0, D):
            print(dash, end='')
        ans = int(n / 3)
        for l1 in range(0, ans):
            print(dot, end='')
            print(vert_bar, end='')
            print(dot, end='')
        for m1 in range(0, D):
            print(dash, end='')
        print()