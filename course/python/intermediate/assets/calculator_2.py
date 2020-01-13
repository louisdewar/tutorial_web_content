def calculate(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

while True:
    operator = input("Enter the operator (+, -, *, /): ")

    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        # Not a valid operator so tell the user 
        print(operator + ' is not a valid operator')
        # Go back to the start of the while loop
        continue
    
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    equation = str(a) + " " + operator + " " + str(b)

    print(equation + " = " + str(calculate(operator, a, b)))

    should_stop = input("Type yes to stop (hit enter to continue): ")

    if should_stop == "yes":
        break
