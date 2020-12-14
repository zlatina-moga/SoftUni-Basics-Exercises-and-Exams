vineyard = int(input())
grape_per_mt = float(input())
wine_for_sale = int(input())
workers = int(input())

grape = (vineyard * grape_per_mt) * 0.4
wine = grape / 2.5

import math

if wine >= wine_for_sale:
    wine = math.floor(wine)
    extra = wine - wine_for_sale
    extra = math.ceil(extra)
    staff_wine = extra / workers
    staff_wine = math.ceil(staff_wine)
    print(f"Good harvest this year! Total wine: {wine} liters.")
    print(f"{extra} liters left -> {staff_wine} liters per person.")
else:
    difference = wine_for_sale - wine
    difference = math.floor(difference)
    print(f"It will be a tough winter! More {difference} liters wine needed.")
