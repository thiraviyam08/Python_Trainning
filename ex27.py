a=int(input("Enter the total Number of array elements:"))
count=0
num=[]
for i in range(0,a):
    b=int(input("Enter the array element:"))
    num.append(b)
print(num)
for i in num:
    for j in num:
        if(i==j):
            count+=1
    if count>=2:
        print("True")
        break
    else:
        print("False")
        break
