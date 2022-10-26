def po(a,l):
    s=len(a[0])
    d=[int(a[0])]
    for i in a:
        if len(i)==s:
            d.append(int(i))
        elif len(i)<s:
            continue
        elif len(i)>s:
            s=len(i)
            d.clear()
            d.append(int(i))
    return d

s=int(input())
q=list(map(str,input().split()))
print(*po(q,s))