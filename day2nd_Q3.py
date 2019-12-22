# Q3 find whether given number is armstrong or not

def armstrong() :

    x = int(input('enter a number to check if it is armstrong or not'))
    a = x
    b = 0

    while (a != 0):
        d = a % 10
        b = b + pow(d,3)
        a = a//10

    if (x == b):
        print( x ,' is a armstrong number')
    else :
        print(x , ' is not a armstrong number')

armstrong()

