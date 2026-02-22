import random
# computer chose any random number
computer = random.choice([0, 1, 2])
#Ask user choice 
print('Keys: S = Snake, W = Water, G = Gun')
you = input("Enter your Choice: ").lower()
#It assign keys to the values
youDict = {"s": 0, "w": 1, "g": 2}
reverseDict = {0: "Snake", 1: "Water", 2: "Gun"}

#It check user input is valid or not
if you not in youDict:
    print("Invalid Choice!")
    exit()

youchose = youDict[you]
#It tell us user and computer choice
print(f"You Chose: {reverseDict[youchose]}\nComputer Chose: {reverseDict[computer]}")

if(computer == youchose):
    print("It's a Draw!")

elif(computer == 1 and youchose == 2):
    print("You Lose!")

elif(computer == 1 and youchose == 0):
    print("You Win!")

elif(computer == 0 and youchose == 2):
    print("You Win!")

elif(computer == 0 and youchose == 1):
    print("You Lose!")

elif(computer == 2 and youchose == 0):
    print("You Lose!")

elif(computer == 2 and youchose == 1):
    print("You Win!")

else:
    print("Something went wrong!")