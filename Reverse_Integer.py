def po(n):
    c=[]
    if n<0:
        c.append("-")
        n=(-2*n)+n
        while n:
           s=n%10
           n=n//10
           c.append(s)
        return mo(c)
              
    else:
        while n:
            s=n%10
            n=n//10
            c.append(s)
        return mo(c)
def mo(a):
    if "-" in a:
        d=a[::-1]
        for i in range(len(d)-2,-1,-1):
            if d[i]==0:
                d.remove(d[i])
            else:
                break
        return d[::-1]
    else:
        d=a[::-1]
        for i in range(len(d)-1,-1,-1):
            if d[i]==0:
                d.remove(d[i])
            else:
                break
        return d[::-1]
        
       
d=int(input())
p=po(d)
for v in p:
    print(v,end="")




