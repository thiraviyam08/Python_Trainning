n=input("Enter the String:")
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
    if count>1:
        print(i)
