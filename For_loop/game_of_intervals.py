n = int(input())

entry_number_1 = 0
entry_number_2 = 0
entry_number_3 = 0
entry_number_4 = 0
entry_number_5 = 0
invalid_number = 0
total = 0
points = 0


for i in range(1, n + 1):
    entry_number = int(input())
    if 0 >= entry_number <= 9:
        entry_number_1 = 0.2 * entry_number
        entry_number_1 += entry_number
        total += entry_number_1
    elif 10 >= entry_number <= 19:
        entry_number_2 = 0.3 * entry_number
        entry_number_2 += entry_number_2
        total += entry_number_2
    elif 20 >= entry_number <= 29:
        entry_number_3 = 0.4 * entry_number
        entry_number_3 += entry_number_3
        total += entry_number_3
    elif 30 >= entry_number <= 39:
        entry_number_4 = 50
        entry_number_4 += entry_number_4
        total += entry_number_4
    elif 40 >= entry_number <= 50:
        entry_number_5 = 100
        entry_number_5 += entry_number_5
        total += entry_number_5
    else:
        invalid_number = total / 2
        total += invalid_number

percent_1 = entry_number_1 / n
percent_2 = entry_number_2 / n
percent_3 = entry_number_3 / n
percent_4 = entry_number_4 / n
percent_5 = entry_number_5 / n
percent_6 = invalid_number / n

print(f"{total:.2f}")
print(f"From 0 to 9: {percent_1:.2f}%")
print(f"From 10 to 19: {percent_2:.2f}%")
print(f"From 20 to 29: {percent_3:.2f}%")
print(f"From 30 to 39: {percent_4:.2f}%")
print(f"From 40 to 50: {percent_5:.2f}%")
print(f"Invalid numbers: {percent_6:.2f}%")