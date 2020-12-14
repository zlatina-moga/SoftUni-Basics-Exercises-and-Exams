budget = float(input())
extras = int(input())
clothes = float(input())

decor = budget * 0.1

if extras >= 150:
    clothes = clothes - (clothes * 0.1)

clothing_sum = extras * clothes
total = decor + clothing_sum

if total <= budget:
    print("Action!")
    print(f"Wingard starts filming with {abs(total - budget):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget - total):.2f} leva more.")
