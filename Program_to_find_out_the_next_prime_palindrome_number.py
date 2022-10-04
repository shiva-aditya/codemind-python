import math
def po(a):
    i=a+1
    while True:
        if pal(i):
            return i
        else:
            i+=1

def pal(b):
    if prime(b):
        c=str(b) #123
        s=c[::-1] #321
        return c==s
    else:
        return False

def prime(n):
    if n<=1:
        return False
    t=int(math.sqrt(n))
    for i in range(2,t+1):
        if n%i==0:
            return False
    return True


o=int(input())
print(po(o))
