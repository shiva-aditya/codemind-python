def po(a):
    c=[]
    for i in a:
        c.append(len(i))
    return c





w=input()
w=w.split()
print(*po(w))