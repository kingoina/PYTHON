import  logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

machineResources = {
    "water":300,
    "milk":200,
    "coffee":100,
    "money": 0
}
denominations = {
    "quarters": 0.25,
    "nickel": 0.10,
    "dimes": 0.05,
    "pennies": 0.01,
}

quatity = [300, 200, 100]
units = ["ml", "ml", "g", "$"]

profit = 0

def report(resources, resourceunits):
    index = 0
    for resource in resources :
        print(f"{resource} : {resources.get(resource)}{resourceunits[index]}")
        index += 1

def restock():
    machineResources["water"] = 300
    machineResources["milk"] = 200
    machineResources["coffee"] = 100
    print("Machine restocked successfully.")


def coinSystem(coins):
    global profit
    for coin in coins:
        money = int(input(f"how many {coin}?:")) * coins[coin]
        profit += round(money, 2)



def drink():
    global profit, is_On
    drinkChoice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drinkChoice in ["espresso", "latte", "cappuccino"]:
        coinSystem(denominations)

        if profit > MENU[drinkChoice]["cost"]:
            change = round(profit - MENU[drinkChoice]["cost"], 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {drinkChoice} ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")

        for ingredient in MENU[drinkChoice]["ingredients"]:

            if machineResources[ingredient] - MENU[drinkChoice]["ingredients"][ingredient] <= 0:
                print(f"Sorry there is not enough {ingredient}.Please restock")
            else:
                machineResources[ingredient] = machineResources[ingredient] - MENU[drinkChoice]["ingredients"][ingredient]

        machineResources["money"] += MENU[drinkChoice]["cost"]

    elif drinkChoice == "report":
        report(machineResources, units)

    elif drinkChoice == "off" :
        print("It was nice offering you a drink.Goodbyee 💕💕")
        is_On = False

    elif drinkChoice == "restock":
        restock()
        report(machineResources, units)

    else:
        print("Please enter a valid drink or command🙏")

print(logo.art)
is_On = True
while is_On:
    drink()
