# #size 3
#
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
#
# #size 5
#
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
#
# #size 10
#
# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------

size = 10
linelen = 4 * size - 3
reverserep = []
for i in range(1, size + 1):
    s = ""
    for j in range(1, i + 1):
        s += chr(97 + size - j)
    for k in range(1, i):
        s += chr(97 + size - i + k)
    r = "-".join(s)
    reverserep.append(r)
    print(r.center(linelen, "-"))
for l in range(1, size):
    print(reverserep[size - l - 1].center(linelen, "-"))


# def print_rangoli(size):
#     height = 2 * size - 1
#     width = 2 * height - 1
#
#     l = []
#     next_mid = chr(96 + size)
#
#     for i in range(size, -size + 1, -1):
#         if i == size:
#             # first character
#             l.append(next_mid)
#         elif i in range(size, 0, -1):
#             # top and middle
#             middle = len(l) // 2
#             previous_mid = next_mid
#             next_mid = chr(96 + i)
#             l.insert(middle, next_mid)
#             l.insert(middle, previous_mid)
#         else:
#             # bottom
#             middle = len(l) // 2
#             l.pop(middle)
#             l.pop(middle)
#         string = '-'.join(l)
#         string = string.center(width, '-')
#         print(string)
#
# def print_rangoli(size):
#     lett = 'abcdefghijklmnopqrstuvwxyz'
#
#     for i in range(-size + 1, size):
#         for j in range(-size + 1, size):
#             charPos = abs(i) + abs(j)
#             if charPos < size:
#                 print(lett[charPos], end='')
#             else:
#                 print('-', end='')
#
#             if j < size - 1:
#                 print('-', end='')
#             else:
#                 print('')
