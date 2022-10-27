def po(a):
    t="aeiou"
    r="AEIOU"
    c=0
    for i in a:
        if i[0] in t:
            if i[-1] not in t:
                c+=1
        elif i[0] in r:
            if i[-1] not in t:
                c+=1
    return c

w=input()
w=w.split()
print(po(w))