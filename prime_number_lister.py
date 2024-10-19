import random
def checkIfPrime(a):
    n=0
    for i in range(2,int(a/2)+1):
        if a%i == 0:
            n+=1
        else:
            pass
    if n>0:
        return False
    else:
        return True

    return En
a=int(input("Enter number where the range starts: "))
if a==1:
    a+=1
b=int(input("Enter number where the range ends: "))
E=[]
for i in range(a,b):
    if checkIfPrime(i):
        E.append(i)
print(random.choice(E))
print(E)
