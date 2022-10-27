def po(a):
    a=set(a)
    return len(a)
    
w=input()
w=w.lower()
w=w.split()
w="".join(w)
print(po(w))
