fuel_type = input()
quantity = float(input())
club_card = input()

cost = 0
if fuel_type == "Gasoline":
    cost = quantity * 2.22
    if club_card == "Yes":
        cost -= quantity * 0.18
    else:
        cost = quantity * 2.22
elif fuel_type == "Gas":
    cost = quantity * 0.93
    if club_card == "Yes":
        cost -= quantity * 0.08
    else:
        cost = quantity * 0.93
elif fuel_type == "Diesel":
    cost = quantity * 2.33
    if club_card == "Yes":
        cost -= quantity * 0.12
    else:
        cost = quantity * 2.33
if 20 <= quantity <= 25:
    cost -= cost * 0.08
elif quantity > 25:
    cost -= cost * 0.1

print(f"{cost:.2f} lv.")