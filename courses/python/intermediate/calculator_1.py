def calculate(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

# Should print 5 (since 2+3)
print(calculate('+', 2, 3))
 
# Should print 11 (since 13-2)
print(calculate('-', 13, 2))
 
# Should print 2 (since 5/2)
print(calculate('/', 10, 5))
 
# Should print 40 (since 5/2)
print(calculate('*', 2, 20))
