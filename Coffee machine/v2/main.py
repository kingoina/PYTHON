
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import art

machine = CoffeeMaker()
money = MoneyMachine()
drinks = Menu()

drinksArray = {"latte":0, "espresso":1, "cappuccino":2 }


def coffeeMachine():


    choice = input(f"What drink would you like from these ?{drinks.get_items()}: ").lower()
    if choice == "report":
        machine.report()
        money.report()

    elif choice == "off":
        print("Thank for taking coffee with us.")
        return False

    elif choice == "restock":
        machine.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        print("Coffee machine successfully restocked.")

    elif  drinks.find_drink(choice):
        # The variable below initialize the MenuItem class from menu.py
        drink =  drinks.menu[drinksArray[choice]]
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)
        else:
            print("Please restock the ingredients")
    return True
print(art)
is_On = True
while is_On:
    is_On = coffeeMachine()