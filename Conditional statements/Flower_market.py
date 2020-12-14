num_of_magnolias = int(input())
num_of_zumbuls = int(input())
num_of_roses = int(input())
num_of_cacti = int(input())
gift_price = float(input())

flower_price = (num_of_magnolias * 3.25)+(num_of_zumbuls * 4)+(num_of_roses * 3.5)+(num_of_cacti * 8)
total_price = flower_price - (flower_price * 0.05)

import math
difference = total_price - gift_price
difference = math.floor(difference)
change = gift_price - total_price
change = math.ceil(change)

if total_price >= gift_price:
    print(f"She is left with {difference} leva.")
else:
    print(f"She will have to borrow {change} leva.")