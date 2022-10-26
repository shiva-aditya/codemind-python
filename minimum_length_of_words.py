def po(a):
    c=[]
    for i in a:
        c.append(len(i))
    return min(c)




s=input()
s=s.split()
print(po(s))