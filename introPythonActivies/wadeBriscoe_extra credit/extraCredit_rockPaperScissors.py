import random

def makeYourChoice():
    print ("press r for Rock")
    print ("press p for Paper")
    print ("press s for Scissors")
    print("press q to Quit!")
    userChoice = raw_input("what do you want to choose?")

    if userChoice == "r":
        return "Rock"
    if userChocie == "p":
        return "Paper"
    if userChoice == "s":
        return "Scissors"
    if userChoice == "q":
        
        sys.exit (0)
    else:
        makeYourChoice()


    