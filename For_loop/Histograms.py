n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
total_p1 = 0
total_p2 = 0
total_p3 = 0
total_p4 = 0
total_p5 = 0

for i in range(1, n + 1):
    current_number = int(input())
    if current_number < 200:
        p1 = current_number
        total_p1 += 1
        p1 = total_p1 / n * 100
    elif current_number <= 399:
        p2 = current_number
        total_p2 += 1
        p2 = total_p2 / n * 100
    elif current_number <= 599:
        p3 = current_number
        total_p3 += 1
        p3 = total_p3 / n * 100
    elif current_number <= 799:
        p4 = current_number
        total_p4 += 1
        p4 = total_p4 / n * 100
    else:
        p5 = current_number
        total_p5 += 1
        p5 = total_p5 / n * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")