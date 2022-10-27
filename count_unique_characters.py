def po(a):
    q=set(list(a))
    c=0
    for i in q:
        if a.count(i)==1:
            c+=1
    return c
    
w=input()
w=w.lower()
w=w.split()
w="".join(w)
print(po(w))