def po(a,b):
    r=set(a)
    y=set(b)
    p=list(r&y)
    return len(p)

w=input()
w=w.lower()
w=w.split()
e=input()
e=e.lower()
e=e.split()
print(po(w,e))