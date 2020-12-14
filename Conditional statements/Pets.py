days = int(input())
total_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

dog = days * dog_food
cat = days * cat_food
turtle = days * (turtle_food / 1000)
all_food = dog + cat + turtle
import math
difference = total_food - all_food
difference = math.floor(difference)
diff = abs(all_food - total_food)
diff = math.ceil(diff)

if total_food >= all_food:
    print(f"{difference} kilos of food left.")
else:
    print(f"{diff} more kilos of food are needed.")