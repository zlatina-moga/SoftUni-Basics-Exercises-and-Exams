moves = 0
total_points = 0
point_1 = 0
point_2 = 0
point_3 = 0
point_4 = 0
point_5 = 0
invalid_num = 0

for i in range(1, moves + 1):
    number = int(input())
    if 0 >= number <= 9:
        points = 0.2 * number
        point_1 = points
        total_points += points
    elif 10 >= number <= 19:
        points = 0.3 * number
        point_2 = points
        total_points += points
    elif 20 >= number <= 29:
        points = 0.4 * number
        point_3 = points
        total_points += points
    elif 30 >= number <= 39:
        points = 50
        point_4 = points
        total_points += points
    elif 40 >= number <= 50:
        points = 100
        point_5 = points
        total_points += points
    else:
        invalid_num = total_points / 2
        invalid_num += invalid_num

point_1_percent = point_1 / total_points * 100
point_2_percent = point_2 / total_points * 100
point_3_percent = point_3 / total_points * 100
point_4_percent = point_4 / total_points * 100
point_5_percent = point_5 / total_points * 100
invalid_percent = invalid_num / total_points * 100


print(f"{total_points:.2f}")
print(f"From 0 to 9: {point_1_percent:.2f}%")
print(f"From 10 to 19: {point_2_percent:.2f}%")
print(f"From 20 to 29: {point_3_percent:.2f}%")
print(f"From 30 to 39: {point_4_percent:.2f}%")
print(f"From 40 to 50: {point_5_percent:.2f}%")
print(f"Invalid numbers: {invalid_percent:.2f}%")