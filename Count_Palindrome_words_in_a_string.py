def po(a):
    c=0
    for i in a:
        t=i[::-1]
        if t==i:
            c+=1
    return c



w=input()
w=w.lower()
w=w.split()
print(po(w))