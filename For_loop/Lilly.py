age = int(input())
washing_mashine = float(input())
toy_price = int(input())

toys = 0
money = 0
total = 0
toy_money = 0
bonus = 10

for i in range(1, age + 1):
    if i % 2 == 1:
        toys += 1
        toy_money = toys * toy_price
    else:
        money += bonus - 1
        bonus += 10

total = money + toy_money

if total >= washing_mashine:
    extra = total - washing_mashine
    print(f"Yes! {extra:.2f}")
else:
   diff = washing_mashine - total
   print(f"No! {diff:.2f}")