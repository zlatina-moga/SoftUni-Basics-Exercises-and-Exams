start = int(input())
end = int(input())
magic_num = int(input())
is_found = False
combinations = 0

for first in range(start, end + 1):
    for second in range(start, end+1):
        combinations += 1
        if first+second == magic_num:
            print(f"Combination N:{combinations} ({first} + {second} = {magic_num})")
            is_found = True
            break
    if is_found :
        break
if not is_found:
    print(f"{combinations} combinations - neither equals {magic_num}")



