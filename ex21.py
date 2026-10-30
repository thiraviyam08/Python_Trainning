a=input()
b=a.split()
for i in a:
    f=0
    for j in a:
        if i==j:
            f+=1
            c=f
    print(c)
c=sorted(b)
print(c)
