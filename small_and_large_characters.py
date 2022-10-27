def po(a):
    c=[]
    for i in a:
        c.append(min(i))
        c.append(max(i))
    return c
    
w=input()
w=w.lower()
w=w.split()
print(*po(w))