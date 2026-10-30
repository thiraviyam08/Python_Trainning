a=input("Enter any lines:")
b=["a","e","i","o","u","A","E","I","O","U"]
c=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N"]
vowels=0
cons=0
for i in a:
    if i in b:
        vowels+=1
    if i in c:
        cons+=1
print(vowels)
print(cons)
