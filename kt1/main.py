import random

goodbye_count = 0

print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")
while True:
    user_input = input("> ")

    if "ПОКА" in user_input:
        goodbye_count += 1
        if goodbye_count == 3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
            break
        else:
            year = random.randint(1930, 1950)
            print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
    elif user_input.isupper():
        year = random.randint(1930, 1950)
        print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
    else:
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
