def po(a):
    q=list(set(a))
    for i in a:
        if a.count(i)==1:
            return i
    return -1
    
w=input()
w=w.lower()
print(po(w))