number = float(input())
converting_from = input()
converting_to = input()

number_in_m = 0

if converting_from == "mm":
    number_in_m = number / 1000
elif converting_from == "cm":
    number_in_m = number / 100
else:
    number_in_m = number

result = 0

if converting_to == "mm":
    result = number_in_m * 1000
elif converting_to == "cm":
    result = number_in_m * 100
else:
    result = number_in_m

print(f"{result:.3f}")