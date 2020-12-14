puzzle = 2.6
talking_doll = 3
teddy_bear = 4.1
minion = 8.2
truck = 2

excursion_prise = float(input())
number_of_puzzles = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

sum = puzzle * number_of_puzzles + talking_doll * number_of_talking_dolls + teddy_bear * number_of_teddy_bears + minion * number_of_minions + truck * number_of_trucks

total_number = number_of_trucks + number_of_minions + number_of_teddy_bears + number_of_talking_dolls + number_of_puzzles

if total_number >= 50:
    sum -= sum * 0.25
sum -= sum * 0.1

if sum >= excursion_prise:
    print(f"Yes! {sum - excursion_prise:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_prise - sum:.2f} lv needed.")



