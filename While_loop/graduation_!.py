student = input()
year = 1
is_failed = False
grades_total = 0

while year <= 12:
    yearly_grade = float(input())

    if yearly_grade < 4:
        if is_failed:
            break
        is_failed = True
        continue

    year += 1
    grades_total += yearly_grade

if year < 12:
    print(f"{student} has been excluded at {year} grade")
else:
    print(f"{student} graduated. Average grade: {grades_total / 12:.2f} ")
