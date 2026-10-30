a=int(input("Enter the total number of elements in an array:"))
b=[]
c=[]
for i in range(0,a):
    d=int(input("Enter the First array element:"))
    b.append(d)
print(b)
for i in range(0,a):
    d=int(input("Enter second array element:"))
    c.append(d)
print(c)
b=(set(b))
c=(set(c))
print(b&c)
