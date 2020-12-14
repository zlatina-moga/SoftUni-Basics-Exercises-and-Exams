days = int(input())
hours = int(input())
total = 0
fee = 0
counter = 0

for day in range(1, days + 1):
    counter += 1
    daily_fee = 0
    for hour in range(1, hours+1):
        if day % 2 == 0 and hour % 2 == 1:
            fee = 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            fee = 1.25
        else:
            fee = 1
        total += fee

        daily_fee += fee
    print(f"Day: {counter} - {daily_fee:.2f} leva")

print(f"Total: {total:.2f} leva")


