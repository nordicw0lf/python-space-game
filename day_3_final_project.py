print('''
     _
                     ,' '.
                    /     \
                  ^ |  _  | ^
                 | || / \ || |
                 | |||.-.||| |
                 | |||   ||| |
                 | |||   ||| |
                 | |||   ||| |
                 | |||   ||| |
                 | ,'     '. |
                 ,'__     __`.
                /____  |  ____\
                 /_\ |_|_| /_\
                 .:   : :   :.
                 : .  : .  : :
                  ::   ::   ::
                 : : .: :. : :
                .: :.: : :. : .
                : : .: :  ::  :
            .:  .   : :   ..
''')
print("welcome to the space game!")
print("your mission is to find your way to Mars using Elon Musk's SpaceX rocket")

choice_1 = input("where would you like to start, by flying left or right? ")
if choice_1 == "right":
    print("you fell into a black hole, and you are now dead :(")
    print("game over, see you next time!")
elif choice_1 == "left":
    print("you are now continuing on the right path!")
else:
    print("Invalid choice! game over, see you next time!")

if choice_1 != "right":
    choice_2 = input('''you have come across alien spaceships, they seem friendly, but you are not sure what to do,
 would you like to wait for them to pass or attack? ''')
    if choice_2 == "attack":
        print("you have been overpowered by the aliens, they shot you with their lasers, and you are now dead :(")
        print("game over, see you next time!")
    elif choice_2 == "wait":
        print("Look at you still making progress! good job!")

        choice_3 = input('''you have come across 3 wormholes, the first one is red, the second one is blue, the third one is yellow, 
what wormhole would you want to risk going through? ''')
        if choice_3 == "red":
            print("you have entered a wormhole that devoured you with fire, and you are now dead :(")
            print("game over, see you next time!")
        elif choice_3 == "blue":
            print("you have entered a wormhole full of strange man-eating aliens, you are now dead :(")
            print("game over, see you next time!")
        elif choice_3 == "yellow":
            print("You have entered the wormhole that has delivered you safely to Mars! Good job!")
        else:
            print("Invalid choice! game over, see you next time!")
    else:
        print("Invalid choice! game over, see you next time!")
