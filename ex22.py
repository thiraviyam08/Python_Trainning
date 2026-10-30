"""
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
"""
n=int(input("Enter the Totoal Numbers of List:"))
a=[]
b=[]
num=[]
for i in range(0,n):
    m=int(input("Number:"))
    num.append(m)
for i in num:
    if i==0:
        b.append(i)
    else:
        a.append(i)
print(a+b,end="")
