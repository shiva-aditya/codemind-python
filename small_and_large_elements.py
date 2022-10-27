def po(a):
    c=[]
    c.append(min(a[0]))
    c.append(max(a[-1]))
    return c
    
    
    
w=input()
w.lower()
w=w.split()
print(*po(w))