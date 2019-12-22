

# Q5
alist  = ['kidney' , 45 , 78.9 ]
print(alist)
n = input("enter the number u want to remove from above list")

for i in alist :
    if str(n) == i:
       alist.remove(n)

print(alist)
