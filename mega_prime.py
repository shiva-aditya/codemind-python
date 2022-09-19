import math
def po(n):
    if prime(n):
        c=[]
        while n:
            r=n%10
            n=n//10
            c.append(r)
        for i in c:
            if prime(i):
                continue
            else:
                return "Not Mega Prime"
        return "Mega Prime"
    else:
        return "Not Mega Prime"



def prime(a):
    if a==1:
        return False
    g=int(math.sqrt(a))
    for i in range(2,g+1):
        if a%i==0:
            return False
    return True
    
    
i=int(input())
print(po(i))
        