import random
import time
import os

mycards = []
file = []


def run():
    global randnum, randnum0
    randnum0 = random.randint(1, 22)
    randnum = random.randint(1, 22)
    question = input("What Must You Know?: ")
    game = input(
        "What Reading Do You Want?: \n 1: Single Card \n 2: Past, Present, Future \n 3: 4-Card Spread \n Selection: ")
    with open("tarotcards.txt") as f:
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
            fourcard()


def fourcard():
    def rerun(selection):
        print("Shuffling... ")
        time.sleep(5)
        if randnum0 != selection:
            print(file[selection])

        elif randnum0 == selection:
            pass

    rerun(randnum)

    def choicenum1():
        global randnum2
        choice = input("Do You Like Your Card?: ").lower()
        randnum2 = random.randint(1, 22)
        if choice == 'yes':
            print("Shuffling... ")
            time.sleep(5)
            mycards.append("First Card: " + file[randnum])
            print(file[randnum2])
            choicenum2()

        elif choice == 'no':
            rerun(randnum2)
            choicenum1()

    def choicenum2():
        global randnum3
        choice2 = input("Do you like this card?: ").lower()
        randnum3 = random.randint(1, 22)
        if choice2 == 'yes':
            print("Shuffling... ")
            time.sleep(5)
            mycards.append("Second Card: " + file[randnum2])
            print(file[randnum3])
            choicenum3()

        elif choice2 == 'no':
            rerun(randnum3)
            choicenum2()

    def choicenum3():
        global randnum4
        choice3 = input("How About This Card?: ").lower()
        randnum4 = random.randint(1, 22)
        if choice3 == 'yes':
            print("Shuffling... ")
            time.sleep(5)
            mycards.append("Third Card: " + file[randnum3])

            print(file[randnum4])
            choicenum4()

        elif choice3 == 'no':
            rerun(randnum3)

    def choicenum4():
        choice4 = input("What about this last card?")
        if choice4 == 'yes':
            mycards.append("Last Card: " + file[randnum4])
            os.system('cls' if os.name == 'nt' else 'clear')
            print(mycards[0] + '\n')
            print(mycards[1] + '\n')
            print(mycards[2] + '\n')
            print(mycards[3] + '\n')
            run()

        elif choice4 == 'no':
            rerun(randnum4)

    choicenum1()


run()
