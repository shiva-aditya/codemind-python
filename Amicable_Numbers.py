def po(n,m):
    c=1
    for i in range(2,n):
        if n%i==0:
            c=c+i
    if c==m:
        return "Amicable"
    else:
        return "Not Amicable"
    
    
a=int(input())
b=int(input())
print(po(a,b))