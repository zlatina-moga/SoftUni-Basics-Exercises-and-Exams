hour = int(input())
minutes = int(input())

minutes = minutes + 15

if minutes > 59:
    hour = hour + 1
    minutes = minutes - 60

if hour > 23:
    hour = hour - 24

if 0 <= minutes <= 9:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")



