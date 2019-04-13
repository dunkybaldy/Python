def Subtract(x, y):
    return x - y
def Add(x, y):
    return x + y
def Multiply(x, y):
    return x * y
def Divide(x, y):
    return x / y
def Modulo(x, y):
    return x % y

validOptions = ["+", "-", "/", "*", "%"]
functions = [Add, Subtract, Divide, Multiply, Modulo]

firstNumber = float(input("What is your first number?\r\n"))

validEntry = False
action = None
while not validEntry:
    action = input(f"Which expression do you choose out of the following valid options: {validOptions}?\r\n")
    if action in validOptions:
        validEntry = True
    else:
        print("That is not a valid entry.\r\n")

secondNumber = float(input("What is your second number?\r\n"))

f = functions[validOptions.index(action)]
print(f(firstNumber, secondNumber))