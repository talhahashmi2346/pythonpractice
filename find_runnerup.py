n = int(input('enter range'))
student_marks = {}
for _ in range(n):
    name = input('enter name')
    line = input('enter numbers').split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input('enter query name')
l = len(scores)
ans = 0.00
for i in student_marks:
    if query_name == i:
        ans = float(sum(student_marks[i]) / len(student_marks[i]))
print(round(ans, 2))
