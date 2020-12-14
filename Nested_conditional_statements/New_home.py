flowers = input()
flower_count = int(input())
budget = int(input())

total = 0

if flowers == "Roses":
    total = flower_count * 5
    if flower_count > 80:
        total -= total * 0.1
elif flowers == "Dahlias":
    total = flower_count * 3.8
    if flower_count > 90:
        total -= total * 0.15
elif flowers == "Tulips":
    total = flower_count * 2.8
    if flower_count > 80:
        total -= total * 0.15
elif flowers == "Narcissus":
    total = flower_count * 3
    if flower_count < 120:
        total += total * 0.15
elif flowers == "Gladiolus":
    total = flower_count * 2.5
    if flower_count < 80:
        total += total * 0.2

if total <= budget:
    change = budget - total
    print(f"Hey, you have a great garden with {flower_count} {flowers} and {change:.2f} leva left.")
else:
    change = abs(budget - total)
    print(f"Not enough money, you need {change:.2f} leva more.")