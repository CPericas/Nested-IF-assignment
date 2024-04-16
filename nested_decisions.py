# TASK 1 - CODE CORRECTION
#place = input("Choose a place: forest or cave?: ")

#if place == "forest":
#    action = input("climb a tree or cross a river?: ")
#    if action == "climb a tree":
#        print("You found a bird's nest!")
#    else:
#        print("You found a boat!")
#elif place == "cave":
#    print("You find a hidden treasure!")

#TASK 2 - SETTING THE SCENE
#place = input("Choose a place: forest or cave?: ")

#if place == "forest":
#    action = input("climb a tree or cross a river?: ")
#    if action == "climb a tree":
#        print("You found a bird's nest!")
#    else:
#        print("You found a boat!")
#elif place == "cave":
#    action = input("light a torch or proceed in the dark?: ")
#    if action == "light a torch":
#        print("You find the hidden treasure!")
#    else:
#        print("You fall down a cavern to your demise!")



# TASK 3 - DEFAULT PATH
place = input("Choose a place: forest or cave?: ")

if place == "forest":
    action = input("climb a tree or cross a river?: ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark?: ")
    if action == "light a torch":
        print("You find the hidden treasure!")
    elif action == "proceed in the dark":
        print("You fall down a cavern to your demise!")
    else:
        pass
else:
    pass