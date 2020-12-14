n = int(input())

price = 0
average_price = 0
total_weight = 0
total_price = 0
van_price = 0
truck_price = 0
train_price = 0
weight_van = 0
weight_truck = 0
weight_train = 0

for i in range(1, n+1):
    weight = int(input())
    total_weight += weight
    if weight <= 3:
        weight_van += weight
        price = 200 * weight
    elif weight <= 11:
        weight_truck += weight
        price = 175 * weight
    else:
        weight_train += weight
        price = 120 * weight
    total_price += price

average_price = total_price / total_weight
print(f"{average_price:.2f}")

van_price = weight_van / total_weight * 100
truck_price = weight_truck / total_weight * 100
train_price = weight_train / total_weight * 100

print(f"{van_price:.2f}%")
print(f"{truck_price:.2f}%")
print(f"{train_price:.2f}%")