inherited_money = float(input())
year_of_living = int(input())

spending = 0
age = 0


for i in range(1800, year_of_living + 1):
    age = (i - 1800) + 18
    if i % 2 == 0:
        spending += 12000
    elif i % 2 == 1:
        spending += 12000 + age * 50

if spending <= inherited_money:
    extra = inherited_money - spending
    print(f"Yes! He will live a carefree life and will have {extra:.2f} dollars left.")
else:
    diff = spending - inherited_money
    print(f"He will need {diff:.2f} dollars to survive.")