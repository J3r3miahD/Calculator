# Addition Function
def addition(a, b):
    return a + b

# Subtraction Function
def subtraction(a, b):
    return a - b

# Multiplication Function
def multiplication(a, b):
    return a * b

# Division Function
def division(a, b):
    if a == 0 or b == 0:
        print('Zero division not allowed')
        return 'None'
    return a / b

# Display instructions before starting the program
print("""
Welcome to the Simple Calculator!

This program will allow you to perform basic arithmetic operations: addition, subtraction, multiplication, and division.
You can choose one of the following options:
- 'a' for Addition
- 's' for Subtraction
- 'm' for Multiplication
- 'd' for Division

You will be asked to input two numbers. The program will then perform the selected operation on those numbers and display the result.

You can type 'stop' to exit the program at any time.

Let's begin!
""")

while True:
    print('Enter the function you would like to perform')
    print('\'a\' for Addition')
    print('\'s\' for Subtraction')
    print('\'m\' for Multiplication')
    print('\'d\' for Division')
    print('\'stop\' to exit')
    function = input('Enter selection: ')

    function = function.lower()

    if function in ('a', 's', 'm', 'd'):
        first_value = float(input('Enter your first value: '))
        second_value = float(input('Enter your second value: '))

        if function == 'a':
            print(first_value, ' + ', second_value, ' = ', addition(first_value, second_value))
        elif function == 's':
            print(first_value, ' - ', second_value, ' = ', subtraction(first_value, second_value))
        elif function == 'm':
            print(first_value, ' * ', second_value, ' = ', multiplication(first_value, second_value))
        elif function == 'd':
            print(first_value, ' / ', second_value, ' = ', division(first_value, second_value))
        print('\n')

    elif function == 'stop':
        print('Exiting...')
        break
    else:
        print("Invalid selection, please choose a valid operation ('a', 's', 'm', 'd') or 'stop' to exit.\n")
