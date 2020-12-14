kilometers = int(input())
time = input()
transport = 0

if kilometers < 20 and time == "day":
    transport = (0.79 * kilometers) + 0.7
    print(f"{transport:.2f}")
elif kilometers < 20 and time == "night":
    transport = (0.9 * kilometers) + 0.7
    print(f"{transport:.2f}")
elif kilometers < 100 :
    transport = 0.09 * kilometers
    print(f"{transport:.2f}")
else:
    transport = 0.06 * kilometers
    print(f"{transport:.2f}")


