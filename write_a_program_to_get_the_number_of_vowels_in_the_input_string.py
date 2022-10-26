def po(a):
    p=["a","e","i","o","u","A","E","I","O","U"]
    c=0
    for i in a:
        if i in p:
            c+=1
    return c




w=input()
print(po(w))