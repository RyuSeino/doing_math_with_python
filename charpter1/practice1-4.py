from fractions import Fraction


def add(a, b):
    print('Result of addition: {0}'.format(a+b))


def sub(a, b):
    print('Result of subtracting: {0}'.format(a-b))


def div(a, b):
    print('Result of dividing {0} by {1} is {2}'.format(a, b, a / b))


def mul(a, b):
    print('Result of multiplying: {0}'.format(a*b))


if __name__ == '__main__':

    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
        if op == 'Add':
            add(a, b)
        elif op == 'Subtract':
            sub(a, b)
        elif op == 'Divide':
            div(a, b)
        elif op == 'Multiply':
            mul(a, b)
    except ValueError:
        print('Error')









