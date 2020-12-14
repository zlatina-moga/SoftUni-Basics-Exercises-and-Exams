capacity = int(input())
total_fans = int(input())

A_fans = 0
B_fans = 0
V_fans = 0
G_fans = 0

for i in range(1, total_fans + 1):
    fan = input()
    if fan == "A":
        A_fans += 1
    elif fan == "B":
        B_fans += 1
    elif fan == "V":
        V_fans += 1
    elif fan == "G":
        G_fans += 1

A_fans = A_fans / total_fans * 100
B_fans = B_fans / total_fans * 100
V_fans = V_fans / total_fans * 100
G_fans = G_fans / total_fans * 100
total = total_fans / capacity * 100

print(f"{A_fans:.2f}%")
print(f"{B_fans:.2f}%")
print(f"{V_fans:.2f}%")
print(f"{G_fans:.2f}%")
print(f"{total:.2f}%")