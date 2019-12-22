# Q3 odd and even numbers in different lists
list = [1,2,3,4,5,6,7,8,9,10]
oddlist = []
evenlist = []

for i in list:
    if i%2 == 0:
        evenlist.append(i)

    else:
        oddlist.append(i)

print("list of even numbers is" , evenlist)
print("list of odd numbers is" , oddlist)

