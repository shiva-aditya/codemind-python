def po(a):
    b=a[0]
    c=[]
    for i in b:
        if mo(a,str(i)):
            if i not in c:
                c.append(i)
    c.sort()
    if len(c)!=0:
        return c[0]
    else:
        return -1

def mo(a,i):
    for k in a:
        if i not in k:
            return False
    return True
    
    
w=input()
w=w.lower()
w=w.split()
print(po(w))