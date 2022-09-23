def po(a,b):
    c=0
    for i in a:
        if pow(i):
            c=c+i
    return c
    
def pow(n):
    if n==1:
        return True
    for i in range(1,n):
        if i*i==n:
            return True
    return False
    
g=int(input())
arr=list(map(int,input().split()))
print(po(arr,g))