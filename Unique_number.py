def po(n):
    for i in n:
        if n.count(i)==1:
            continue
        else:
            return "Not Unique Number"
    return "Unique Number"
    
    
g=input()
print(po(g))