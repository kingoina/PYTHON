from object import Shopkeeper

shop = Shopkeeper()

def client():
    name = input("Could you please share your name: ").upper()

    shop.displayItems(name)

    products = input("\nSelect the item(s) you wish to buy.(separate with a comma):").lower()


    shop.calculatePrice(products)

client()

choice = input("Do you want  to purchase items from our shop?(y/n)").lower()
while(choice == "y"):   
    client()
    choice = input("Do you want  to purchase items from our shop?(y/n)").lower()