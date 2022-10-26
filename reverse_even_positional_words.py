def po(a):
    c=[]
    for i in range(len(a)):
        if i%2==0:
            c.append(a[i][::-1])
        else:
            c.append(a[i])
    return c



w=input()
w=w.split()
print(*po(w))