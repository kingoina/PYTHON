#DAY ONE 
print("Welcome to the band name generator")

city = input("what is the city you grew up in ? \n")
pet = input("What is the name of your first pet? \n")

print(f"Your band name could be  {city}  {pet}")
#DAY TWO
print("Welcome to the tip calculator")

bill = float(input("What was the  total bill?\n$"))
people = int(input("How many peolple to split the bill ? \n$"))
tip =  int(input("What percentage tip would you like to give ? 10, 12, or 15? \n$"))

def tipCalculator(tipPercentage , numberOfPeople, bill):
    fullBill = float((100 + tipPercentage)/100 * bill)
    paymentEach = fullBill / numberOfPeople
    paymentEach = round(paymentEach, 2)
    return paymentEach

val = tipCalculator(tip, people, bill)
print(f"Each person should pay: ${val}")