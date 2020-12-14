months = int(input())

bill = 0
water_bill = 20
internet_bill = 15
others = 0
others_total = 0
average = 0
electricity_total = 0

for i in range(1, months + 1):
    electricity_bill = float(input())
    electricity_total += electricity_bill
    others = ((electricity_bill + 20 + 15) * 0.2)+(electricity_bill + 20 + 15)
    others_total += others


water_bill = water_bill * months
internet_bill = internet_bill * months

average = (electricity_total + water_bill + internet_bill + others_total) / months


print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {others_total:.2f} lv")
print(f"Average: {average:.2f} lv")
