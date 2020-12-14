deposit = float(input())
months = int(input())
simple_rate = 0
complex_rate = 0
deposit_sum = 0

for i in range(months):
    simple_rate += 3 * deposit / 100
simple_rate += deposit
for i in range(months):
    complex_rate = deposit + (deposit * 0.027)

complex_rate += deposit
print(f"Simple interest rate: {simple_rate:.2f} lv.")
print(f"Complex interest rate: {complex_rate:.2f} lv.")
if simple_rate > complex_rate:
    print(f"Choose a simple interest rate. You will win {simple_rate-complex_rate:.2f} lv.")
else:
    print(f"Choose a complex interest rate. You will win {complex_rate-simple_rate:.2f} lv.")

