#add

def add(n1, n2):
    return n1 + n2

#subtraction

def subtraction(n1, n2):
    return n1 - n2

#division

def  division(n1,n2):
    return n1 / n2

#multiplication

def multiply(n1,n2):
    return n1 * n2

operations = {
              "+":add,
              "-":subtraction,
              "/":division,
              "*":multiply
              }

num1 = float(input("Enter the first number: "))



for operand in operations:
    print(operand)
    
operand = input("which operation would you like to perform from the above: ")

num2 = float(input("Enter the second number: "))

function = operations[operand]
answer = function(num1, num2)

print(f"{num1} {operand} {num2} = {answer}")

continue_calculating = True

while continue_calculating:
    
    
    
    if input(f"Type 'y' to continue calculating with {answer} or 'n' to exit") == "y":
        
        operand = input("which operation would you like to perform: ")
        num3 = float(input("what's the next number?"))
        function = operations[operand]
        next_answer = function(answer, num3)
        print(f"{answer} {operand} {num3} = {next_answer}")
        answer = next_answer
    else:
        continue_calculating = False
        print("Byee")
    
    