

def even_or_odd(a):

    if a % 2 == 0:
        print('even')
    else:
        print('odd')


def print_after9_numbers(a):

    tmp = a
    for i in range(0, 9):
        print(tmp + 2)
        tmp += 2



if __name__ == '__main__':
    a = input('enter a number: ')
    even_or_odd(int(a))
    print_after9_numbers(int(a))

