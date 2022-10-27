def po(a):
    b=a[0]
    c=[]
    for i in b:
        if mo(a,str(i)):
            c.append(i)
    if len(c)!=0:
        for i in c:
            print(i,end="")
    else:
        print(-1)

def mo(a,i):
    for k in a:
        if i not in k:
            return False
    return True
    
w=input()
w=w.lower()
w=w.split()
po(w)