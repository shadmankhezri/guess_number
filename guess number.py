# Number guessing game
# You can guess number among 2 to 12
# The computer guesses two numbers and compares their sum with your number
import random
while True:
        print("\t╔════════════════════╗")
        print("\t║"+"      ◄ MENU ►      "+"║")
        print("\t║"+"                    "+"║")
        print("\t║"+"Play »              "+"║")
        print("\t║"+"                    "+"║")
        print("\t║"+"Exit »              "+"║")
        print("\t║"+"                    "+"║")
        print("\t║"+"                    "+"║")
        print("\t╚════════════════════╝\n")
        x = input("Enter y for plying the game or n for exit: ")
        if x == "n":
            print("\t○○○ EXIT SUCCESSFULY ○○○\n")
            break
        elif x == "y":
            def play ():
                for i in range(1 , 4):
                    your_num = int(input(f"{i}th guess = Enter your number among (2,12): "))
                    print(f"\nyour number = {your_num}")
                    num1 , num2 = (random.randint(1 , 6) , random.randint(1 , 6))
                    sum = num1 +num2
                    if your_num == sum:
                        print(f"computer guess is ({num1} , {num2}) and guess sum = {sum}\n")
                        print("\t☼☼☼ Your Win ☼☼☼\n\n")
                        break
                    else:
                        print(f"computer guess is ({num1} , {num2}) , guess sum = {sum}\n")
                        print("\t◄◄◄ Your Wrong ►►►\n")
            play()
