'''
1 for snake
-1 for water
0 for gun'''
import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")
youDict = {'s': 1, 'w': -1, 'g': 0}
you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

reverseDict = {1: 'snake', -1: 'water', 0: 'gun'}

print(f"Computer chose {reverseDict[computer]}")
print(f"You chose {reverseDict[you]}")

if(computer == you):
    print("It's a tie!")

else:
    if(computer == -1 and you == 1):
        print("You win!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer == 0 and you == 1):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You win!")

    elif(computer == 0 and you == -1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You lose!")

    else:
        print("Something went wrong")

print("Thanks for playing!")

