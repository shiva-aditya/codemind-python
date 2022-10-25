def po(a,l):
    if l%2==0:
        e=a[:l//2:]
        w=a[l//2::]
    else:
        e=a[:(l//2)+1:]
        w=a[(l//2)+1::]
    if len(e)==len(w):
        print(sum(e))
        print(sum(w))
    else:
        w.append(e[-1])
        e.pop()
        print(sum(e))
        print(sum(w))

s=int(input())
q=list(map(int,input().split()))
po(q,s)