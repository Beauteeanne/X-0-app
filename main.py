# str1 = input("Enter a word: ")
# str2 = input("Enter another word: ")
# sorted_str1 = sorted(str1)
# sorted_str2 = sorted(str2)
#
# if len(str1) == len(str2):
#     if sorted_str1 == sorted_str2:
#         print("true")
#     else:
#         print("false")

import random
myList = ["R", "S", "P"]
r = input("Choose a letter from myList: ")

sample_list = random.choice(myList)

def my_function(r):
    for x in r:
        if( "sample_list == r"):
            print("Rock beats scissors")
        elif("r == sample_list"):
            print("Scissors beats paper")
        else:
            ("paper beats scissors")
my_function(r)





