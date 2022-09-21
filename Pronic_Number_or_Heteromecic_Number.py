import math
def po(n):
    f=int(math.sqrt(n))
    for i in range(1,f+1):
        if i*(i+1)==n:
            return "YES"
    return "NO"
    
    
d=int(input())
print(po(d))