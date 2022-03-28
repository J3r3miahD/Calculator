# Addition Function
def addition(x, y):
    return x + y

# Subtraction Function
def subtraction(x, y):
    return x - y

# Multiplication Function
def multiplication(x, y):
    return x * y

# Division Function
def division(x, y):
    if x == 0 or y == 0:
        print('zero division not allowed')
        return 'None'
    return x / y

while True:
    print('Enter the function you would like to perform')
    print('\'a\' for Addition')
    print('\'s\' for Subtraction')
    print('\'m\' for Multiplication')
    print('\'d\' for Division')
    print('\'stop\' to exit')
    fun = input('Enter selection: ')

    fun = fun.lower()

    if fun in ('a', 's', 'm', 'd'):
        x = float(input('Enter your first value: '))
        y = float(input('Enter you second value: '))

        if fun == 'a':
            print(x, ' + ', y, ' = ', addition(x, y))
        elif fun == 's':
            print(x, ' - ', y, ' = ', subtraction(x, y))
        elif fun == 'm':
            print(x, ' * ', y, ' = ', multiplication(x, y))
        elif fun == 'd':
            print(x, ' / ', y, ' = ', division(x, y))
        print('\n')

    else:
        print('exit')
        break
