
def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))


def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))


def fahrenheit_celsius():
    fahrenheit = float(input('Enter temperature in fahrenheit: '))
    celsius = (fahrenheit - 32) * (5 / 9)
    print('temperature in celsius: {0}'.format(celsius))


def celsius_fahrenheit():
    celsius = float(input('Enter temperature in celsius: '))
    fahrenheit = celsius * (9 / 5) + 32
    print('temperature in fahrenheit: {0}'.format(fahrenheit))


def kilograms_pounds():
    kilograms = float(input('Enter weight in kilograms: '))
    pounds = kilograms * 2.2046
    print('weight in pounds: {0}'.format(pounds))


def pounds_kilograms():
    pounds = float(input('Enter weight in pounds: '))
    kilograms = pounds / 2.2046
    print('weight in kilograms: {0}'.format(kilograms))




def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Fahrenheit to Celsius')
    print('4. Celsius to Fahrenheit')
    print('5. Kilograms to Pounds')
    print('6. Pounds to Kilograms')


if __name__ ==  '__main__':
    print_menu()
    choice = input('which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
    if choice == '3':
        fahrenheit_celsius()
    if choice == '4':
        celsius_fahrenheit()
    if choice == '5':
        kilograms_pounds()
    if choice == '6':
        pounds_kilograms()


