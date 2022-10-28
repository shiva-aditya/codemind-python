def po(a,b):
    r=set(a)
    y=set(b)
    q=list(r&y)
    c=0
    for i in q:
        if a.count(i)==b.count(i):
            c+=1
    return c




w=input()
w=w.split()
e=input()
e=e.split()
print(po(w,e))
