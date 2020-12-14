year = input()
holidays = int(input())
weekends = int(input())

volleyball = 0
import math

sofia_volley = (48 - weekends) * 3/4
holiday_volley = holidays * 2/3

volleyball = sofia_volley + holiday_volley + weekends

if year == "leap":
    volleyball += volleyball * 0.15
volleyball = math.floor(volleyball)
print(volleyball)