import random
choices=['s','w','g']
chances=10
intial=1
computer=0
user=0
while(intial<=chances):
    userchoice = input("choose between S snake W water G gun")
    ran = random.choice(choices)
    userchoice = userchoice.lower()
    if userchoice==ran:
        print("tie you both choose the same players\nno points")
    elif userchoice == "s" and ran == "g":
        print(f"You choose {userchoice} and computer choose {ran}\ngun kills snake\nComputer won")
        computer=computer+1
    elif userchoice == "g" and ran == "s":
        print(f"You choose {userchoice} and computer choose {ran}\ngun kills snake\nUser won")
        user=user+1
    elif userchoice == "w" and ran == "g":
        print(f"You choose {userchoice} and computer choose {ran}\ngun drowns in water\nUser won")
        user=user+1
    elif userchoice == "g" and ran == "w":
        print(f"You choose {userchoice} and computer choose {ran}\ngun drowns in water\nComputer won")
        computer=computer+1
    elif userchoice == "s" and ran == "w":
        print(f"You choose {userchoice} and computer choose {ran}\nsnake drank water\nUser won")
        user = user +1
    elif userchoice == "w" and ran == "s":
        print(f"You choose {userchoice} and computer choose {ran}\nsnake drank water\nComputer won")
        computer = computer + 1
    else:
        print("enter a valid input You can choose between S(Snake) W(water) G(Gun)")
    print("number of chances left:"+str(int(chances)-int(intial)))
    intial = intial + 1
    if intial>chances:
        print("game over")

print(f"Your score is {user} and computer score is {computer}")
if user<computer:
    print("Computer won the game")
elif user==computer:
    print("Its a tie you both scored same points")
else:
    print("user won")








