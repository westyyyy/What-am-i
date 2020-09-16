def valid(question):
    answer = input(question + "\n> ")
    while not(answer == "y" or answer == "n"):
        answer = input(question + "\n> ")
    if answer == "y":
        return True
    return False

print ("Welcome to what am I\nRespond with y/n\n")
if valid("Does it have legs?"):
    
    if valid("Does it have wings?"):
        print ("It's a bird!")
    elif valid("Does it live in a cage?"):
        if valid("Is it a hamster?"):
            print ("It's a hamster!")
    else:
        if valid("Does it live indoors?"):
            if valid("Is it a cat?"):
                print ("It's a cat!")
            else:
                print ("It's a dog!")
        else:
            print ("It's a fox!")
elif valid("Does it live underwater?"):
    if valid("Is it a fish?"):
        print ("It's a fish!")
    else:
        print ("It's a snake!")
else:
    print("It's a snake!")
