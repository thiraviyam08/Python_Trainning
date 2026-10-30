a=input("Enter a first string:")
b=input("Enter a second string:")
c=0
if len(a)==len(b):
    for i in a:
        if i in b:
            c+=1
    if c==len(a):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")
#Alternative:
"""
a=input("Enter a first string:")
b=input("Enter a second string:")
if sorted(a)== sorted(b):
    print("Anagram")
else:
    print("Not Anagram")
"""

