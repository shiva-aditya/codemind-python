def po(n,m):
    t=1
    i=2
    while n>=i and m>=i:
        if n%i==0 and m%i==0:
            n=n//i
            m=m//i
            t=t*i
        else:
            i+=1
    return t*n*m

a,b=map(int,input().split())
print(po(a,b))