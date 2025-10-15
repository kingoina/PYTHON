import random as num
from art import logo

print(logo)

AI_guess = num.randint(1, 100)
print("Welcome to the number guessing game!")
print("Am thinking pf a number btn 1 and 100")

choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

PLAYER_lives = 0

# if anything other than "hard" is typed it deafult to easy mode
if choice == "hard":
    PLAYER_lives = 5
else :
    PLAYER_lives = 10
    
PLAYER_guess = int(input("Make a guess: "))

def guessChecker():
  if PLAYER_guess > AI_guess:
    print("Too high. \nGuess again.")   
    print(f"You have {PLAYER_lives} attempts remaining to guess the  number.")
  elif PLAYER_guess < AI_guess:
    print("Too low. \nGuess again.")
    print(f"You have {PLAYER_lives} attempts remaining to guess the  number.") 

restart = False 
while not restart:
  guessChecker()
  PLAYER_lives -= 1
  
  PLAYER_guess = int(input("Make a guess: "))
  
  if PLAYER_guess == AI_guess:
    print(f"You win.The number is {PLAYER_guess}")
    restart = True  
    
  elif PLAYER_lives == 0:
    print(f"You Lose.Your lives were depleted.{AI_guess} was th number")    
    restart = True  
    
    

