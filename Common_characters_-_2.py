def po(a):
    b=a[0]
    c=0
    for i in b:
        if mo(a,str(i)):
            c+=1
    return c

def mo(a,i):
    for k in a:
        if i not in k:
            return False
    return True
    
w=input()
w=w.lower()
w=w.split()
print(po(w))