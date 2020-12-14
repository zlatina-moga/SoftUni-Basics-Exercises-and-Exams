total_floors = int(input())
total_rooms = int(input())

for floors in range(total_floors, 0, -1):
    room_type = ""
    if floors == total_floors:
        room_type = "L"
    elif floors % 2 == 1:
        room_type = "A"
    else:
        room_type = "O"

    for rooms in range(total_rooms):
        print(f"{room_type}{floors}{rooms}", end=" ")

    print()
