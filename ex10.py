a=input("Enter the string:")
for i in a:
    if a.count(i)==1:
        print(i)
        break
#Alternative code
"""
n=input("")
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
    if count==1:
        print(i)
        break
"""
