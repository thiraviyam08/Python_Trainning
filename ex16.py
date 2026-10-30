n=input("Enter the string:")
a=n.split()
b=["A","E","I","O","U","a","e","i","o","u"]
c=0
for i in a:
    i=i[0]
    if i in b:
        c+=1
print(c)
