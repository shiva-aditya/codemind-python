def po(a):
    p=1
    s=0
    while a:
        d=a%10
        a=a//10
        p=p*d
        s=s+d
    if s==p:
        return "Spy Number"
    else:
        return "Not Spy Number"
        
i=int(input())
print(po(i))