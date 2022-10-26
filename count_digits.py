def po(a):
    d=[]
    for i in a:
        d.append(len(str(abs(i))))
    return d



s=int(input())
q=list(map(int,input().split()))
print(*po(q))