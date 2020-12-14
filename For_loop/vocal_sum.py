text = input()

total = 0

for index in range(0, len(text)):
    symbol = text[index]
    if symbol == "a":
        total += 1
    elif symbol == "e":
        total += 2
    elif symbol == "i":
        total += 3
    elif symbol == "o":
        total += 4
    elif symbol == "u":
        total += 5
print(total)