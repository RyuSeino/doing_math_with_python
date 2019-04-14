
def multi_table(a, b):
    for i in range(1, b+1):
        print('{0} x {1} = {2}'.format(a, i, a * i))


if __name__ == '__main__':
    a = input('enter a number: ')
    b = input('Enter the number of multiples: ')
    multi_table(int(a), int(b))

