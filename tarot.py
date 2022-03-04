import os
import time
import random


class App:
    def __init__(self):
        self.mycards = []
        self.file = []
        with open("tarotcards.txt") as f:
            for line in f.readlines():
                self.file.append(line)

    def check(self, game):
        if int(game) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Your Question For The Universe: " + self.question + '\n')
            print("Shuffling Deck... ")
            time.sleep(5)
            print(self.file[self.randnum])
            input("Enter to Continue... ")
            os.system('cls' if os.name == 'nt' else 'clear')
            self.run()

        elif int(game) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Your Question For The Universe: " + self.question + '\n')
            print("Shuffling Deck... ")
            time.sleep(5)
            randnum2 = random.randint(0, 21)
            randnum3 = random.randint(0, 21)
            if randnum2 == self.randnum:
                randnum2 = random.randint(0, 21)
                randnum3 = random.randint(0, 21)
            if randnum3 == self.randnum or randnum3 == randnum2:
                randnum3 = random.randint(0, 21)

            print("Past: " + self.file[self.randnum])
            print("Present: " + self.file[randnum2])
            print("Future: " + self.file[randnum3])
            input("Enter to Continue... ")
            os.system('cls' if os.name == 'nt' else 'clear')
            self.run()

        elif int(game) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')
            self.fourcard()

    def run(self):
        global randnum, randnum0
        self.randnum0 = random.randint(0, 21)
        self.randnum = random.randint(0, 21)
        self.question = input("What Must You Know?: ")
        self.comp()

    def comp(self):
        game = input(
            "What Reading Do You Want?: \n 1: Single Card \n 2: Past, Present, Future \n 3: 4-Card Spread \n Selection: ")
        if game.isdigit() is False:
            if game.lower() == 'q' or game.lower() == 'quit':
                pass
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Numbers ONLY!")
                return self.comp()
        elif int(game) <= 3 or int(game) >= 1:
            self.check(game)
        elif int(game) >= 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Only Numbers 1-3...  ")
            return self.comp()
        else:
            print("Restarting...  ")
            return self.comp()

    def fourcard(self):
        def choicenum1():
            global randnum2
            randnum2 = random.randint(0, 21)
            time.sleep(1)
            print("Shuffling... ")
            time.sleep(5)
            print(self.file[randnum2])
            choice = input("Do You Like Your Card?: ").lower()
            if choice == 'yes' or choice == 'y':
                self.mycards.append("First Card: " + self.file[randnum2])
                choicenum2()

            elif choice == 'no' or choice == 'n':
                os.system('cls' if os.name == 'nt' else 'clear')
                return choicenum1()

        def choicenum2():
            global randnum3
            randnum3 = random.randint(0, 21)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Shuffling... ")
            time.sleep(5)
            print(self.file[randnum3])
            choice2 = input("Do you like this card?: ").lower()
            if choice2 == 'yes' or choice2 == 'y':
                self.mycards.append("Second Card: " + self.file[randnum2])
                choicenum3()

            elif choice2 == 'no' or choice2 == 'n':
                os.system('cls' if os.name == 'nt' else 'clear')
                return choicenum2()

        def choicenum3():
            global randnum4
            randnum4 = random.randint(0, 21)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Shuffling... ")
            time.sleep(5)
            print(self.file[randnum4])
            choice3 = input("How About This Card?: ").lower()
            if choice3 == 'yes' or choice3 == 'y':
                self.mycards.append("Third Card: " + self.file[randnum3])
                choicenum4()

            elif choice3 == 'no' or choice3 == 'n':
                os.system('cls' if os.name == 'nt' else 'clear')
                return choicenum3()

        def choicenum4():
            global randnum5
            randnum5 = random.randint(0, 21)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Shuffling... ")
            time.sleep(5)
            print(self.file[randnum5])
            choice4 = input("What about this last card?:  ")
            if choice4 == 'yes' or choice4 == 'y':
                self.mycards.append("Last Card: " + self.file[randnum4])
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Your Cards:  ")
                for names in self.mycards:
                    print(names.split(':')[1])
                print('\n')
                print(self.mycards[0] + '\n')
                print(self.mycards[1] + '\n')
                print(self.mycards[2] + '\n')
                print(self.mycards[3] + '\n')
                print("^ Cards Above...  ^")
                input("Press Any Key To Continue...  ")
                os.system('cls' if os.name == 'nt' else 'clear')
                self.run()

            elif choice4 == 'no' or choice4 == 'n':
                return choicenum4()

        choicenum1()


if __name__ == "__main__":
    app = App()
    app.run()
