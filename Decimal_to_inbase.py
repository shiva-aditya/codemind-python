def po(n,b):
    s=[]
    while n:
        t=n%b
        n=n//b
        s.append(t)
    m=0
    c=0
    for i in s:
        if (i==0):
            c+=1
        else:
            if (c>m):
                m=c
            c=0
    if (m==0):
        return -1
    else :
        return m
            
s=int(input())
e=int(input())
print(po(s,e))