def po(n):
    c=[]
    while n:
        r=n%10
        n=n//10
        c.append(r) 
    g=c[::-1] 
    return g==c 
for _ in range(int(input())):   
    o=int(input())
    print(po(o))
        