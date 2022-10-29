def po(h):
    a=0
    e=0
    i=0
    o=0
    u=0
    A=0
    E=0
    I=0
    O=0
    U=0
    for k in h:
        if k=="a":
            a+=1
        elif k=="e":
            e+=1
        elif k=="i":
            i+=1
        elif k=="o":
            o+=1
        elif k=="u":
            u+=1
        elif k=="A":
            A+=1
        elif k=="E":
            E+=1
        elif k=="I":
            I+=1
        elif k=="O":
            O+=1
        elif k=="U":
            U+=1
    if (a and e and i and u and o) or (A and E and I and O and U):
        return True
    else:
        return False

w=input()
print(po(w))
