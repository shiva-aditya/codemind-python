def po(a):
    c=[]
    for i in a:
        c.append(len(i))
    return max(c)
    
w=input()
w=w.split()
print(po(w))