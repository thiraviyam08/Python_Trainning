a=input("Enter the string:")
b=input("Enter the character:")
count=0
for i in a:
    if i in b:
        count+=1
print(count)
