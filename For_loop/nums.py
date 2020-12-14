n = int(input())

import sys
total = 0
max_num = -sys.maxsize


for i in range(1, n + 1):
    num = int(input())
    if max_num < num:
        max_num = num
    total += num

total -= max_num

if total == max_num:
    print("Yes")
    print(f"Sum = {total}")
else:
    diff = abs(total - max_num)
    print("No")
    print(f"Diff = {diff}")