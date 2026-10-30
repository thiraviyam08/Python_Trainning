a=input()
for i in a:
    if ord(i)>=65 and ord(i)<=90:
        print(i.lower(),end="")
    elif ord(i)>=97 and ord(i)<=122:
        print(i.upper(),end="")
    elif ord(i)>=48 and ord(i)<=56:
        print(i,end="")
    else:
        continue
