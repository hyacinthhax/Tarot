import random
import time
import os


def run():
    question = input("What Must You Know?: ")
    game = input(
        "What Reading Do You Want?: \n 1: Single Card \n 2: Past, Present, Future \n 3: 4-Card Spread \n Selection: ")
    file = []
    with open("tarotcards.txt") as f:
        randnum = random.randint(1, 22)
        for line in f.readlines():
            file.append(line)

        if int(game) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Shuffling... ")
            time.sleep(10)
            print(question)
            print(file[randnum])
            input("Enter to Continue... ")
            os.system('cls' if os.name == 'nt' else 'clear')
            run()

        elif int(game) == 2:
            pass

        elif int(game) == 3:
            pass


run()
