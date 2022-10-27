def po(a):
    c=0
    t="aeiou"
    for i in a:
        for j in range(len(i)//2):
            if i[j] in t and i[len(i)-1-j] not in t:
                c+=1
            elif i[j] not in t and i[len(i)-1-j] in t:
                c+=1
    return c
    
w=input()
w=w.split()
print(po(w))