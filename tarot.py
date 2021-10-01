import random
import time
import os

mycards = []
file = []
with open("tarotcards.txt") as f:
        for line in f.readlines():
            file.append(line)

def check(game):
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

def run():
    global randnum, randnum0, question
    randnum0 = random.randint(1, 22)
    randnum = random.randint(1, 22)
    question = input("What Must You Know?: ")
    def comp():
        game = input("What Reading Do You Want?: \n 1: Single Card \n 2: Past, Present, Future \n 3: 4-Card Spread \n Selection: ")
        if game.isdigit() is False:
            if game.lower() == 'q' or game.lower() == 'quit':
                pass
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Numbers ONLY!")
                comp()
        elif int(game) <= 3:
            check(game)
        elif int(game) >= 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Only Numbers 1-3...  ")
            comp()


    comp()



def fourcard():
    with open("tarotcards.txt") as f:
        for line in f.readlines():
            file.append(line)
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
                if choice == 'yes' or choice == 'y':
                    print("Shuffling... ")
                    time.sleep(5)
                    mycards.append("First Card: " + file[randnum])
                    print(file[randnum2])
                    choicenum2()

                elif choice == 'no' or choice == 'n':
                    rerun(randnum2)
                    choicenum1()

            def choicenum2():
                global randnum3
                choice2 = input("Do you like this card?: ").lower()
                randnum3 = random.randint(1, 22)
                if choice2 == 'yes' or choice2 == 'y':
                    print("Shuffling... ")
                    time.sleep(5)
                    mycards.append("Second Card: " + file[randnum2])
                    print(file[randnum3])
                    choicenum3()

                elif choice2 == 'no' or choice2 == 'n':
                    rerun(randnum3)
                    choicenum2()

            def choicenum3():
                global randnum4
                choice3 = input("How About This Card?: ").lower()
                randnum4 = random.randint(1, 22)
                if choice3 == 'yes' or choice3 == 'y':
                    print("Shuffling... ")
                    time.sleep(5)
                    mycards.append("Third Card: " + file[randnum3])

                    print(file[randnum4])
                    choicenum4()

                elif choice3 == 'no' or choice3 == 'n':
                    rerun(randnum3)

            def choicenum4():
                choice4 = input("What about this last card?")
                if choice4 == 'yes' or choice4 == 'y':
                    mycards.append("Last Card: " + file[randnum4])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(mycards[0] + '\n')
                    print(mycards[1] + '\n')
                    print(mycards[2] + '\n')
                    print(mycards[3] + '\n')
                    run()

                elif choice4 == 'no' or choice4 == 'n':
                    rerun(randnum4)

            choicenum1()


run()
