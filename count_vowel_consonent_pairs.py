def po(a):
    c=0
    t="aeiou"
    for i in range(len(a)//2):
       # print(a[i],a[len(a)-1-i])
        if a[i] in t:
            if a[len(a)-1-i]==" ":
                continue
            if a[len(a)-1-i] not in t:
                c+=1
                #print(c,a[i])
        elif a[len(a)-1-i] in t:
            if a[i]==" ":
                continue
            if a[i] not in t:
                c+=1
               # print(c,a[i])
    return c


w=input()
print(po(w))