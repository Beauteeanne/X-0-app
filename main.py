
import random
myList = ["R", "S", "P"]
user_action = input("Choose a letter from the list (R, P, S): ")
computer_action = random.choice(myList)
def my_function(user_action):

        if user_action == computer_action:
            print("It's a tie")
        if user_action != myList:
             print('Error')
             if computer_action == "R" and user_action == "S":
                 print("Rock beats Scissors")
             elif user_action == "S" and computer_action == "P":
                 print("Scissors beats Paper")
                 if user_action == "P" and computer_action == "R":
                    print("Paper beats Rock")
my_function(user_action)





