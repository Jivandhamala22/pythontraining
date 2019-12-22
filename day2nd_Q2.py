
# Q2 return value of a raised to power b

def pow(a,b) :
    x = a
    for i in range(1,b) :
       a = a * x

    return a

num1 = int(input('enter first number '))
num2 = int(input('enter second number '))

x = pow(num1,num2)
print(num1 , '^^^ ' , num2 , ' is ' , x)

