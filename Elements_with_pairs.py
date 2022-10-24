def po(a):
    if len(a)%2!=0:
        a.append(0)
    return a






s=int(input())
q=list(map(int,input().split()))
print(*po(q))