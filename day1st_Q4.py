

# Q4 sepparate list for integers , floats and strings


list = ["kidney" , 45 , 78.9 , 12.05 , "apple" , 4 , "jivan" , 44 ]
intlist = []
floatlist = []
stringlist = []
for j in list :

    if (isinstance(j,int)):
        intlist.append(j)

    elif (isinstance(j,str)):
        stringlist.append(j)

    else :
        floatlist.append(j)

print("list of integers is",intlist)
print("list of floating values is",floatlist)
print("list of strings is",stringlist)
