# Import the random module
import random
import time

# Define a function to print a message with a delay

def print_pause(message):
    print(message)
    time.sleep(4)

# Define a function to start the game
def start_game():
    # Initialize the score to zero
    score = 0
    # Print the introduction
    print_pause("Welcome to the Adventure Game!")
    print_pause("You are an explorer who is looking for a treasure in a mysterious land.")
    print_pause("You have a map that shows two possible locations where the treasure might be hidden.")
    print_pause("One is a dark cave and the other is a sunny beach.")
    # Ask the player to choose a location
    location = input("Where do you want to go? (cave or beach)\n >>")
   # while location =="cave" or "beach":
    # Call the appropriate function based on the player's choice
    if location == "cave":
        cave(score)
    elif location == "beach":
        beach(score)
        # break
    while location != "cave" or "beach":
          location = input("please enter (cave or beach)\n>>")
          if location == "cave":
              cave(score)
          elif location == "beach":
              beach(score)
          else:
              location = input ("please enter (cave or beach)\n>>")
              if location == "cave":
                  cave(score)
              elif location == "beach":
                  beach(score)

# Define a function for the cave scenario
def cave(score):
    # Print the description of the cave
    print_pause("You enter the cave and see a dim light at the end of it.")
    print_pause("You walk towards the light and find a chest with a lock on it.")
    print_pause("You also see a skeleton holding a key in its hand.")
    # Ask the player to choose an action
    action = input("What do you want to do? (take the key (take) or( leave )\n >>")
   # while action =="take" or "leave":
    # Call the appropriate function based on the player's choice
    if action == "take":
        take_key(score)
    elif action == "leave":
        leave(score)
         # break
    while action != "take" or "leave":
          action = input("please enter (take) or (leave)\n >>")
          if action == "take":
              take_key(score)
          elif action == "leave":
              leave(score)
          else:
              action = input("please enter (take) or (leave)\n >>")
              if action == "take":
                  take_key(score)
              elif action == "leave":
                  leave(score)



# Define a function for taking the key from the skeleton
def take_key(score):
    # Print the outcome of taking the key
    print_pause("You approach the skeleton and try to take the key from its hand.")
    print_pause("Suddenly, the skeleton comes to life and attacks you!")
    # Generate a random number between 1 and 10
    number = random.randint(1, 10)
    # If the number is less than or equal to 5, the player wins the fight
    if number <= 5:
        print_pause("You manage to fight off the skeleton and grab the key.")
        print_pause("You open the chest and find a pile of gold coins inside.")
        print_pause("You have found the treasure!")
        # Increase the score by 10 points
        score += 10
        # Call the end_game function with True as an argument
        end_game(True, score)
    # If the number is greater than 5, the player loses the fight
    else:
        print_pause("The skeleton is too strong for you and knocks you down.")
        print_pause("You lose consciousness and never wake up again.")
        print_pause("You have failed your quest.")
        # Call the end_game function with False as an argument
        end_game(False, score)

# Define a function for leaving the cave without taking the key
def leave(score):
    # Print the outcome of leaving the cave
    print_pause("You decide to leave the cave and look for another way to find the treasure.")
    print_pause("You walk back to where you started and see another path leading to a beach.")
    # Ask the player if they want to go to the beach or not
    choice = input("Do you want to go to the beach? (yes(y) or no(n)\n >>")
    #while choice == "y" or "n":

    # Call the appropriate function based on the player's choice
    if choice == "y":
        beach(score)
    elif choice == "n":
        print_pause("You decide to stay where you are and wait for someone to rescue you.")
        print_pause("Unfortunately, no one ever comes and you die of hunger and thirst.")
        print_pause("You have failed your quest.")
        # Call the end_game function with False as an argument
        end_game(False, score)
         # break
    while choice != "y" or "n":
        choice = input("please enter (yes(y) or no(n)\n >>")
        if choice == "y":
            beach(score)
        elif choice == "n":
            print_pause("You decide to stay where you are and wait for someone to rescue you.")
            print_pause("Unfortunately, no one ever comes and you die of hunger and thirst.")
            print_pause("You have failed your quest.")
            # Call the end_game function with False as an argument
            end_game(False, score)
        else:
            choice = input("please enter (yes(y) or no(n)\n >>")
            if choice == "yes":
                beach(score)
            elif choice == "no":
                print_pause("You decide to stay where you are and wait for someone to rescue you.")
                print_pause("Unfortunately, no one ever comes and you die of hunger and thirst.")
                print_pause("You have failed your quest.")
                # Call the end_game function with False as an argument
                end_game(False, score)

# Define a function for the beach scenario
def beach(score):
    # Print the description of the beach
    print_pause("You arrive at a sunny beach and see a boat anchored near the shore.")
    print_pause("You also see a sign that says 'Beware of sharks'.")
    # Ask the player to choose an action
    action = input("What do you want to do? (swim to the boat(swim) or stay on land (stay)\n >>")
   # while action == "swim" or "stay":
    if action == "swim":
        swim(score)
    elif action == "stay":
        stay(score)
    #    break
          # Call the appropriate function based on the player's choice
    while action != "swim" or "stay":
          action = input("please enter (swim) or (stay)\n >>")
          if action == "swim":
             swim(score)
          elif action == "stay":
               stay(score)
          else:
              action = input("please enter (swim) or (stay)\n >>")
              if action == "swim":
                  swim(score)
              elif action == "stay":
                  stay(score)

# Define a function for swimming to boat from beach
def swim(score):
     # Print outcome of swimming
     print_pause ("You decide to swim towards boat hoping it has treasure.")
     print_pause ("As you get closer, you notice something moving under water.")
     print_pause ("It's a shark and it's heading straight for you!")
     # Generate random number between 1 and 10
     number = random.randint(1,10)
     # If number is less than or equal 5, player wins fight
     if number <=5:
         print_pause ("You manage to punch shark in nose and scare it away.")
         print_pause ("You reach boat and climb aboard.")
         print_pause ("You find chest with jewels inside.")
         print_pause ("You have found treasure!")
         # Increase score by 10 points
         score +=10
         # Call end_game function with True as argument
         end_game(True,score)
     # If number is greater than 5, player loses fight
     else:
         print_pause ("The shark bites your leg and drags you under water.")
         print_pause ("You lose blood and drown.")
         print_pause ("You have failed your quest.")
         # Call end_game function with False as argument
         end_game(False,score)

# Define a function for staying on land from beach
def stay(score):
     # Print outcome of staying on land
     print_pause ("You decide to stay on land and look for clues.")
     print_pause ("You find footprints leading to a palm tree.")
     print_pause ("You follow them and see something shiny hanging from tree.")
     # Ask player if they want to climb tree or not
     choice = input ("Do you want climb tree? (yes(y) or no(n)\n>>")
    # while choice == "y" or "n":
           # Call appropriate function based on player's choice
     if choice == "y":
         climb_tree(score)
     elif choice == "n":
         dont_climb_tree(score)
          # break

     while choice != "y" or "n":
           choice = input("please enter (y) or (n)\n>>")
           if choice == "y":
              climb_tree(score)
           elif choice == "n":
                dont_climb_tree(score)
           else:
               choice = input("please enter (y) or (n)\n>>")
               if choice == "y":
                   climb_tree(score)
               elif choice == "n":
                   dont_climb_tree(score)

# Define function for climbing tree from land
def climb_tree(score):
      # Print outcome of climbing tree
      print_pause ("You decide climb tree see what shiny thing is.")
      print_pause ("As you get closer, you realize it's necklace made of pearls.")
      print_pause ("You grab it and put it around your neck.")
      print_pause ("You have found part of treasure!")
      # Increase score by 5 points
      score +=5
      # Call end_game function with True as argument
      end_game(True,score)

# Define function for not climbing tree from land
def dont_climb_tree(score):
      # Print outcome of not climbing tree
      print_pause ("You decide not climb tree afraid of falling.")
      print_pause ("You walk back where you started hope find another clue.")
      print_pause ("Unfortunately, you don't find anything else and waste time.")
      print_pause ("Suddenly, you hear helicopter flying above you.")
      print_pause ("It's your rival explorer who has found treasure before you.")
      print_pause ("He laughs at you and flies away with treasure.")
      print_pause ("You have failed your quest.")
      # Call end_game function with False as argument
      end_game(False,score)

# Define a function for ending game
def end_game(win,score):
       # Print final message based on win argument
       if win:
           message = "Congratulations! You have completed your quest successfully."
       else:
           message = "Sorry! You have failed your quest miserably."
       message += f" Your final score is {score} points."
       message += " Thank you for playing Adventure Game!"
       message += "\n"
       message += "Do you want play again? (yes(y) or no(n))\n >>"
       replay = input(message)
       if replay == "y":
           start_game()
       elif replay == "n":
           exit()
       else:
           invalid_input()

# Define invalid_input() helper method that prints error message when user enters invalid input.
def invalid_input():
   message = "Invalid input. Please enter yes(y) or no(n).\n >>"
   replay = input(message)
  # while replay == "y" or "n":
   if replay == "y":
       start_game()
   elif replay == "n":
       exit()
      #  break
   while replay != "y" or "n":
        ask = "please enter y or n \n >>"
        again = input(ask)
        if again == "y":
            start_game()
        elif again == "n":
            exit()
        else:
            ask = "please enter y or n\n >>"
            again = input(ask)
            if again == "y":
                start_game()
            elif again == "n":
                exit()

start_game()