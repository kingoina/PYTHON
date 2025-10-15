#DAY FOUR
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

items = [rock, paper, scissors]

choicePerson = int(input("What do you choose? Type 0 for Rock, 1 for Paper or  2 for scissors "))

def game():
    randomItem = items[random.randint(0, len(items)-1)]
    print(f"The computer choose:\n {randomItem}")

    indexC_choice = items.index(randomItem)

    if choicePerson == 0 and indexC_choice == 2:
        print("You win")
    if choicePerson == 1 and indexC_choice == 0:
        print("You win")
    if choicePerson == 2 and indexC_choice == 1:
        print("You win")
    if choicePerson == 2 and indexC_choice == 0:
        print("Computer wins")
    if choicePerson == 0 and indexC_choice == 1:
        print("Computer wins")
    if choicePerson == 1 and indexC_choice == 2:
        print("Computer wins")
    if choicePerson == indexC_choice:
        print("Draw")


if choicePerson < 3 and choicePerson >= 0 :
    print(f"You choose:\n {items[choicePerson]}")
    game()
else:
    print("You typed an invalid number, You lose")
