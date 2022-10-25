def po(a,l):
    if l%2==0:
        e=a[:l//2:]
        w=a[l//2::]
    else:
        e=a[:(l//2)+1:]
        w=a[(l//2)+1::]
        w.append(w[-1]+1)
    return abs(sum(e)-sum(w))
    
s=int(input())
q=list(map(int,input().split()))
print(po(q,s))