def po(a):
    ans=[]
    e=["a","e","i","o","u"]
    for i in a:
        if i in e:
            ans.append("V")
        else:
            ans.append("C")
    dub="0"
    for i in ans:
        if dub[-1]==i:
            continue
        else:
            dub=dub+i
    return dub[1::]
s=input()
print(po(s))