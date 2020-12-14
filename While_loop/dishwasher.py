detergent_bottles = int(input())
detergent = detergent_bottles * 750
plates = 0
pans = 0
counter = 0

line = input()
while line != "End":
    line = int(line)

    counter += 1

    if counter == 3:
        detergent -= line * 15
        pans += line
        counter = 0
    else:
        detergent -= line * 5
        plates += line

    if detergent < 0:
        print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
        break
    line = input()

if detergent >= 0:
    print(f"Detergent was enough!")
    print(f"{plates} dishes and {pans} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")



