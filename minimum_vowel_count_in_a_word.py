def po(a):
    ans=[]
    p="aeiou"
    for i in a:
        c=0
        for j in i:
            if j in p:
                c+=1
        ans.append(c)
    return min(ans)
            



w=input()
w=w.lower()
w=w.split()
print(po(w))