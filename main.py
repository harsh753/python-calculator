import math
print('''1. addition
2. subtraction
3. multiplication
4.division
5.square root
6.cube root
7.square
8.cube
9. find cp if loss%
10. find cp if gain%
11. find sp if loss%
12. find sp if gain%
13.to find simple interset
14. to find the compound interset ''')
print('pls type the number corrosponding to the function: ')
print()



def add():
    a=float(input('enter the first number: '))
    b=float(input('enter the second number: '))
    c=a+b
    print(f'sum of {a} and {b} is {c}')

def sub():
    a=float(input('enter the first number: '))
    b=float(input('enter the second number: '))
    c=a-b
    print(f'difference of {a} and {b} is {c}')

def multiplication():
    a=float(input('enter the first number: '))
    b=float(input('enter the second number: '))
    c=a*b
    print(f'product of {a} and {b} is {c}')

def division():
    a=float(input('enter the first number: '))
    b=float(input('enter the second number: '))
    c=a/b
    print(f'qutioent of {a} and {b} is {c}')

def cube_root():
    
    b=float(input('enter the first number: '))
    c=b**(1/3)
    print('cube root of',b,'is',round(c))

def square_root():

    b=float(input('enter the first number: '))
    
    print('square root of',b,'is',math.sqrt(b))

def square():
    b=float(input('enter the number: '))
    c=b*b
    print('square of',b,'is',c)

def cube():
    b=float(input('enter the number: '))
    c=b*b*b
    print('cube of',b,'is',c)

def sp_profit():
    cp = input('Plz type in the C.P. and press enter: ')
    profit = input('Plz type in the profit% and press enter: ')
    print(f'S.P. is {((100 + int(profit)) / 100) * int(cp)} and the formula is: 100 + profit%/100 * cp')

def sp_loss():
    cp = input('Plz type in the C.P. and press enter: ')
    loss = input('Plz type in the loss% and press enter: ')
    print(f'S.P. is {((100 - int(loss)) / 100) * int(cp)} and the formula is: 100 - loss%/100 * cp')


def cp_profit():
    sp = input('Plz type in the S.P. and press enter: ')
    profit = input('Plz type in the profit% and press enter: ')
    print(f'C.P. is {(100 / (100 + int(profit))) * int(sp)} and the formula is: 100 / 100 + profit * sp')


def cp_loss():
    sp = input('Plz type in the S.P. and press enter: ')
    loss = input('Plz type in the loss% and press enter: ')
    print(f'C.P. is {(100 / (100 - int(loss))) * int(sp)} and the formula is: 100 / 100 - loss * sp')

def si():
    principle = input('Type in the p and press enter: ')
    rate = input('Type in the r and press enter: ')
    time = input('Type in the t and press enter: ')
    print(f'S.I. is {int(principle) * int(rate) * int(time) / 100} and the formula is: p*r*t/100')

def a_ci():
    principle = input('Type in p and press enter: ')
    rate = input('Type in r and press enter: ')
    time = input('Type in t and press enter: ')
    print(
        f'Amount is {int(principle) * ((1 + (int(rate) / 100)) ** int(time))} and C.I. is {(int(principle) * ((1 + (int(rate) / 100)) ** int(time))) - int(principle)}')


while True:
    a=input('>>> ')
    if a=='1':
        add()
        print()
        continue
    if a=='2':
        sub()
        print()
        continue
    if a=='3':
        multiplication()
        print()
        continue
    if a=='4':
        division()
        print()
        continue
    if a=='5':
        square_root()
        print()
        continue
    if a=='6':
        cube_root()
        print()
        continue
    if a=='7':
        square()
        print()
        continue
    if a=='8':
        cube()
        print()
        continue
    if a=='9':
        cp_loss()
        print()
        continue
    if a=='10':
        cp_profit()
        print()
        continue
    if a=='11':
        sp_profit()
        print()
        continue
    if a=='12':
        sp_loss()
        print()
        continue
    if a=='13':
        si()
        print()
        continue
    if a=='14':
        a_ci()
        print()
        continue
    if a=='exit':
        exit()
