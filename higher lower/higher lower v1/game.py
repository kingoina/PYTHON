import random, art, data

celebrity_A = random.choice(data.data)
celebrity_B = random.choice(data.data)
score = 0

celebrity = {"A":celebrity_A, "B":celebrity_B}


def gameInfo():
    print(art.logo)
    print(f"Your current score is {score}.")   
    print(f"Compare A: {celebrity_A['name']}, {celebrity_A['description']}, from {celebrity_A['country']}")
    print(art.vs)
    print(f"Compare B: {celebrity_B['name']}, {celebrity_B['description']}, from {celebrity_B['country']}")

gameInfo()

choice = ""

def followerChoice():
    global choice
    choice = input("Who has more followers? Type 'A' or 'B':").upper()
    
    while choice not in ["A", "B"]: 
        print("Please enter a valid choice")
        choice = input("Who has more followers? Type 'A' or 'B':").upper()
        
        
        
     
followerChoice()
      
        
def game():
    global celebrity_A, celebrity_B, celebrity, score, restart
    if choice == "A":
    
        if celebrity[choice]["follower_count"] > celebrity_B["follower_count"]:
            
            score += 1
            restart = True
            # since celebrity_A will be on top no need to shuffle it we only get another random celebrity_b          
            celebrity_B = random.choice(data.data)          
        else:
            print(art.logo)
            print(f"sorry, that's wrong.final score : {score}")
            print(f"{celebrity_B['name']} surpasses {celebrity_A['name']} by {celebrity_B['follower_count'] - celebrity_A['follower_count']} followers")
            restart = False
         
    else:   
        if celebrity[choice]["follower_count"]> celebrity_A["follower_count"]:
            
            score += 1
            restart = True
            
            i = data.data.index(celebrity_B)
            # since celebrity_B  is correct  we reassign  it to celebrity_A  and randomize celebrity_B  
            celebrity_A = data.data[i]
            celebrity_B = random.choice(data.data)
            
        else:
            print(art.logo)
            print(f"sorry, that's wrong.final score : {score}")
            print(f"{celebrity_A['name']} surpasses {celebrity_B['name']} by {celebrity_A['follower_count'] - celebrity_B['follower_count']} followers")
            restart = False
            

restart = False
game()
while  restart: 
    gameInfo()
    followerChoice()
    game()