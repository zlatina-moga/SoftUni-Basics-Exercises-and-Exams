fav_book = input()
current_book = input()
count = 0

while fav_book != current_book:

    if current_book == "No More Books":
        break
    current_book = input()
    count += 1

if current_book == fav_book:
    print(f"You checked {count} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {count} books.")