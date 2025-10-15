#SECRET BIDDING
from art import logo

print(logo)
print("Welcome to the secret auction program")


bidders = []

def dictGenerator ():
    
    name = input("what is your name? :")
    bid = int(input("what is your bid? : $"))
       
    bidders.append({"name": name, "bid": bid}) 


def highestBidder():
    bidSort = []
    for item in bidders:
        bidSort.append(item["bid"])
        
    bidSort.sort()
    bidSort.reverse()
    
    for item in bidders:
        if item["bid"] == bidSort[0]:
            print(f"The winner is {item["name"].upper()} with a bid of ${item["bid"]}.")
        
   
    
others = True
while others:
    dictGenerator()
    result = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    
    if result == "no":
        others = False
        highestBidder()
        
    