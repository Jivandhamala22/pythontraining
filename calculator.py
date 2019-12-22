import  math

def twonum () :
    num1 = int(input(' enter first number'))
    num2 = int(input(' enter second number'))
    return num1 ,num2

def add() :
    m,n = twonum()
    print(m+n)

def sub() :
    m,n = twonum()
    print( m-n)

def mul() :
    m,n = twonum()
    print( m*n)

def div() :
    m,n = twonum()
    print( m/n)

def sqroot() :
    m = int(input('enter a number'))
    print(math.sqrt(m))

def percent() :
    m = int(input('enter a number'))
    print(m/100)

def interest() :
    p,q,r = int(input('give principal , rate of interest , and time'))
    print('interest = ', (p*q*r)/100)

def depriciation() :

x = int(input(''' click anyone  :
1. simple calculator 
2. scientific calculator 
3. business calculator'''))

if x == 1 :

    a = int(input(''' you have entered simple calculator
1. add 
2. subtract
3. multiply
4. percentage
7. division
6. square root
7. cube'''))

    if a == 1 :
        add()

    elif a == 2 :
        sub()

    elif a == 3:
        mul()

    elif a == 4 :
        percent()

    elif a == 5:
        div()

    elif a == 6:
        sqroot()
