def po(w):
    for i in w:
        if w.count(i)>1:
            return False
    return True
    
w=input()
print(po(w))
