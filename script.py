import random
import math
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
def calculatePbKey(p,q):
    n=p*q
    En=(p-1)*(q-1)
    pc=[]
    for i in range(2,En):
        if (math.gcd(i,En)==math.gcd(i,n)==1):
            pc.append(i)
    return random.choice(pc), n
def calculatePvKey(e,En,n):
    Av=[]
    for d in range(1, 10*En):  # Adjust the range as necessary
        if d != e and (d * e) % En == 1:
            Av.append(d)
 #   print(Av)
    return random.choice(Av), n

def error(a):
    if a==101:
        print("The number you inserted is not positive or not a prime number.")
        
############################################################################FUNCTIONS##############################################################################
        
p = int(input('p: '))
if p>1 & checkIfPrime(p):
    q = int(input('q: '))
    if q>1 & checkIfPrime(q):
        print('Good Job!')

        pb = calculatePbKey(p,q)
        En=(p-1)*(q-1)
        n=p*q
        print("Public Key:", pb)
        print("Private Key:", calculatePvKey((pb[0]),En,n))
    
        pass
    else:
        error(101)
else:
    error(101)    
