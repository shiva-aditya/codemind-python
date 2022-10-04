import math
def po(a):
    if prime(a):
        c=str(a)#123
        d=c[::-1]
        if prime(int(d)):
            return "circular prime"
        else:
            return "prime but not a circular prime"
        
    else:
        return "not prime"
        
def prime(n):
    if n<1:
        return False
    w=int(math.sqrt(n))
    for i in range(2,w+1):
        if n%i==0:
            return False
    return True
    
q=int(input())
print(po(q))