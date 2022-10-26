def po(b):
    a=abs(b)
    e=[]
    while a:
        r=a%10
        a//=10
        e.append(r)
    #print(e)
    if e==e[::-1]:
        return True
    
h=int(input())
r=list(map(int, input(). split()))
c=0
for I in r:
    if po(I):
        c+=1
print(c)
