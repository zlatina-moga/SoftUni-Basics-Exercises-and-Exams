eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = 0

for egg in range(eggs):
    color = input()
    if color == "red":
        red_eggs += 1
    elif color == "orange":
        orange_eggs += 1
    elif color == "blue":
        blue_eggs += 1
    elif color == "green":
        green_eggs += 1

    if max_eggs < red_eggs:
        max_eggs = red_eggs
        max_color = "red"
    elif max_eggs < orange_eggs:
        max_eggs = orange_eggs
        max_color = "orange"
    elif max_eggs < blue_eggs:
        max_eggs = blue_eggs
        max_color = "blue"
    elif max_eggs < green_eggs:
        max_eggs = green_eggs
        max_color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {max_color}")