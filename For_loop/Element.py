n = int(input())

total = 0
max_el = 0

for i in range(n):
    curr_el = int(input())
    if max_el < curr_el:
        max_el = curr_el
    total += curr_el

    if i == n-1:
        print(max_el)
        print(total)
        if max_el == total:
            print("Yes")
            print(f"Sum = {i}")
        else:
            diff = abs(max_el - total)
            print("No")
            print(f"Diff = {diff}")