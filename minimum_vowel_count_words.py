def po(a):
    ans=[]
    y="aeiou"
    for i in a:
        c=0
        for j in i:
            if j in y:
                c+=1
        ans.append(c)
    return ans.count(min(ans))




w=input()
w=w.lower()
w=w.split()
print(po(w))