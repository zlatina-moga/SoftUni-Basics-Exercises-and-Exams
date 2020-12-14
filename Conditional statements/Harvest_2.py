wineyard = int(input())
grape = float(input())
wine_liters = int(input())
workers = int(input())

total_grape = wineyard * grape
wine = (0.4 * total_grape) / 2.5
import math

if wine >= wine_liters:
    difference = wine - wine_liters
    wine = math.floor(wine)
    difference = math.ceil(difference)
    workers_wine = difference // workers
    workers_wine = math.ceil(workers_wine)
    print(f"Good harvest this year! Total wine: {wine} liters.")
    print(f"{difference} liters left -> {workers_wine} liters per person.")

else:
    needed_wine = wine_liters - wine
    needed_wine = math.floor(needed_wine)
    print(f"It will be a tough winter! More {needed_wine} liters wine needed.")