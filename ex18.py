stones=input("Enter a stones:")
jewels=input("Enter a jewels:")
count=0
for i in jewels:
    for j in stones:
        if i==j:
            count+=1
print(count)
