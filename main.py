rock = """

       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
"""
paper = """
            ___..__
____..--'''' ._ __.'
              "-..__
            '"--..__";
____        '--...__"";
    `-..__ '"---..._;"
          ''''----

"""
scissors = """
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
"""

get_images  = [rock, paper, scissors]

import random

user_choice = int(input("What do you choose? Type 0 for Rock | 1 for Paper | 2 for Scissors.\n "))

if (user_choice >=3 or user_choice < 0):
    print("You have typed an invalid number. You lose!")
else:
    print("You: " + get_images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer: " + get_images(computer_choice))

    if (user_choice == 0 and computer_choice == 2):
        print("You win!")
    elif (user_choice == 2 and computer_choice == 0):
        print("You lose!")
    elif (user_choice > computer_choice):
        print("You win!")
    elif (user_choice < computer_choice):
        print("You lose!")
    elif (user_choice == computer_choice):
        print("That's a draw!")