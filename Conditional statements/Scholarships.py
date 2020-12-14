income = float(input())
grades = float(input())
min_salary = float(input())

import math
social_scholarship = min_salary * 0.35
social_scholarship = math.floor(social_scholarship)
grades_scholarship = grades * 25
grades_scholarship = math.floor(grades_scholarship)

if income < min_salary and grades > 4.5:
    if grades >= 5.5 and social_scholarship <= grades_scholarship:
        print(f"You get a scholarship for excellent results {grades_scholarship} BGN")
    else:
        print(f"You get a Social scholarship {social_scholarship} BGN")
elif grades >= 5.5:
    print(f"You get a scholarship for excellent results {grades_scholarship} BGN")
else:
    print("You cannot get a scholarship!")
