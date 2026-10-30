s=int(input("Enter the range:"))
count=0
for i in range(1,s+1):
  if i>1:
    if (i==2 or i==3) or (i%2!=0 and i%3!=0):
      print(i)
      count+=1
print("The Count of an Prime Number is",count)
