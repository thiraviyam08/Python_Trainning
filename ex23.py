"""
Given an array nums.
We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
"""
v=int(input("Enter the total number of elements:"))
a=[]
b=[]
sum=0
for i in range(0,v):
    nums = int(input("Enter the Values:"))
    a.append(nums)
for i in a:
    sum+=i
    b.append(sum)
print(a)
print(b)
