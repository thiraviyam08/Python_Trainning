a=input("Enter the string:")
count=0
b=["a","e","i","o","u","A","E","I","O","U"]
for i in a:
    if i in b:
        count+=1
print(count)
