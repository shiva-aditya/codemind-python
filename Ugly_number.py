import math
def po(a):
    if a<0:
        return "Not Ugly Number"
    c=[]
    for i in range(1,a+1):
        if a%i==0:
            c.append(i)
    for t in c:
        if t==1 or t==2 or t==3 or t==5:
            continue
        else:
            if prime(t):
                return "Not Ugly Number"
    return "Ugly Number"
def prime(a):
    if a==1:
        return False
    f=int(math.sqrt(a))
    for i in range(2,f+1):
        if a%i==0:
            return False
    return True
            
    
o=int(input())
print(po(o))