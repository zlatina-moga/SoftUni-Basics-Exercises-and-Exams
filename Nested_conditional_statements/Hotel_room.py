month = input()
nights = int(input())

price_apartment = 0
price_studio = 0

if month == "May" or month == "October":
    price_studio = nights * 50
    price_apartment = nights * 65
    if 7 < nights <= 14:
        price_studio -= price_studio * 0.05
    elif nights > 14:
        price_studio -= price_studio * 0.3
        price_apartment -= price_apartment * 0.1
elif month == "June" or month == "September":
    price_studio = nights * 75.2
    price_apartment = nights * 68.7
    if nights > 14:
        price_studio -= price_studio * 0.2
        price_apartment -= price_apartment * 0.1
elif month == "July" or month == "August":
    price_studio = nights * 76
    price_apartment = nights * 77
    if nights > 14:
        price_apartment -= price_apartment * 0.1
print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")