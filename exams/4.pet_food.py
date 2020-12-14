days = int(input())
total_food = float(input())
dog_food = 0
cat_food = 0
counter = 0
biscuits = 0
total_dog_food = 0
total_cat_food = 0

for day in range(1, days+1):
    dog_food = int(input())
    total_dog_food += dog_food
    cat_food = int(input())
    total_cat_food += cat_food
    together = total_cat_food+total_dog_food
    counter += 1
    if counter % 3 == 0:
        biscuits = (cat_food + dog_food)*0.1

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{together/total_food*100:.2f}% of the food has been eaten.")
print(f"{total_dog_food/together*100:.2f}% eaten from the dog.")
print(f"{total_cat_food/together*100:.2f}% eaten from the cat.")





