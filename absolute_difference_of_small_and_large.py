def po(a):
    c=[]
    for i in a:
        c.append(abs(ord(min(i))-ord(max(i))))
    return c





w=input()
w=w.split()
print(*po(w))