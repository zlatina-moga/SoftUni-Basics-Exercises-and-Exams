n = int(input())

p1 = 0
p2 = 0
p3 = 0

p1_total = 0
p2_total = 0
p3_total = 0

for i in range(1, n + 1):
    current_number = int(input())
    if current_number % 2 == 0:
        p1 = current_number
        p1_total += 1
        p1 = p1_total / n * 100
    if current_number % 3 == 0:
        p2 = current_number
        p2_total += 1
        p2 = p2_total / n * 100
    if current_number % 4 == 0:
        p3 = current_number
        p3_total += 1
        p3 = p3_total / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")