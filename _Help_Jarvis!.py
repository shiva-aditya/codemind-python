def po(a):
    r=[]
    while a:
        d=a%10
        a=a//10
        r.append(d)
    r.sort()
    c=[]
    b=r[0]
    i=0
    while i!=len(r):
        c.append(b)
        b+=1
        i+=1
    if r==c:
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    d=int(input())
    print(po(d))