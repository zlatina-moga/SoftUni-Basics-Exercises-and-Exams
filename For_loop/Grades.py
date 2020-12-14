n = int(input())

grades = 0
average_grade = 0
low_student = 0
medium_student = 0
good_student = 0
very_good_student = 0
total_students = 0

for i in range(1, n+1):
    grade = float(input())
    if 2 <= grade <= 2.99:
        low_student += 1
        grades += grade
    elif 3 <= grade <= 3.99:
        medium_student += 1
        grades += grade
    elif 4 <= grade <= 4.99:
        good_student += 1
        grades += grade
    elif grade >= 5:
        very_good_student += 1
        grades += grade

total_students = low_student+medium_student+good_student+very_good_student

low_student = low_student / total_students * 100
medium_student = medium_student / total_students * 100
good_student = good_student / total_students * 100
very_good_student = very_good_student / total_students * 100
average_grade = grades / total_students

print(f"Top students: {very_good_student:.2f}%")
print(f"Between 4.00 and 4.99: {good_student:.2f}%")
print(f"Between 3.00 and 3.99: {medium_student:.2f}%")
print(f"Fail: {low_student:.2f}%")
print(f"Average: {average_grade:.2f}")

