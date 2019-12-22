# Q4 find whether given number is pallindrome or not

def pallindrome() :

    x = int(input('enter a number to check if it is pallindrome or not'))
    a = x
    b = 0

    while (a != 0):
        b = b * 10
        b = b + (a % 10)
        a = a//10

    if (x == b):
        print( x ,' is a pallindrome number')
    else :
        print(x , ' is not a pallindrome number')

pallindrome()