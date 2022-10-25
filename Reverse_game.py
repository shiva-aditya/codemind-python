def po(a):
    c=[]
    for i in a:
        c.append(int(i[::-1]))
    return c


s=int(input())
q=list(map(str,input().split()))
print(*po(q))