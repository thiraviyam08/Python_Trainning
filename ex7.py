a=1111
a=str(a)
for i in a:
    for j in a[::-5]:
        if i==j:
            print(j,end=" ")
        
