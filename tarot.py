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
            print("Your Question For The Universe: " + question + '\n')
            print("Shuffling Deck... ")
            time.sleep(5)
            print(file[randnum])
            input("Enter to Continue... ")
            os.system('cls' if os.name == 'nt' else 'clear')
            run()

        elif int(game) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Your Question For The Universe: " + question + '\n')
            print("Shuffling Deck... ")
            time.sleep(5)
            randnum2 = random.randint(1, 22)
            if randnum2 == randnum:
                randnum2 = random.randint(1, 22)
            randnum3 = random.randint(1, 22)
            if randnum3 == randnum or randnum3 == randnum2:
                randnum3 = random.randint(1, 22)

            print("Past: " + file[randnum])
            print("Present: " + file[randnum2])
            print("Future: " + file[randnum3])
            input("Enter to Continue... ")
            os.system('cls' if os.name == 'nt' else 'clear')
            run()

        elif int(game) == 3:
            run()


run()
