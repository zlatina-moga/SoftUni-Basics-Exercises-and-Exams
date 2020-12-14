wineyard = int(input())
grape_per_m_sq = float(input())
wine_liters = int(input())
workers = int(input())

wine = ((0.4 * wineyard) * grape_per_m_sq) / 2.5
import math

if wine < wine_liters:
    difference = wine_liters - wine
    difference = math.floor(difference)
    print(f"It will be a tough winter! More {difference} liters wine needed.")
else:
    wine = math.floor(wine)
    print(f"Good harvest this year! Total wine: {wine} liters.")
    wine_left = abs(wine_liters - wine)
    wine_left = math.ceil(wine_left)
    work_wine = abs(wine_left / workers)
    work_wine = math.ceil(work_wine)
    print(f"{wine_left} liters left -> {work_wine} liters per person.")