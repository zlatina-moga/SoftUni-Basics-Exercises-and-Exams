movie = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie != "Finish":
    total = 0
    free_seats = int(input())
    ticket_type = input()
    while ticket_type != "End":

        if total > free_seats:
            break
        if ticket_type == "student":
            student_tickets += 1
            total += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            total += 1
        else:
            kid_tickets += 1
            total += 1
        ticket_type = input()

    print(f"{movie}-{total/free_seats*100:.2f}% full.")
    movie = input()
print(f"Total tickets: {total}")
print(f"{student_tickets/total*100:.2f}% student tickets.")
print(f"{standard_tickets/total*100:.2f}% standard tickets.")
print(f"{kid_tickets/total*100:.2f}% kids tickets.")