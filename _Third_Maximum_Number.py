def po(a,b):
    a=list(set(a))
    a.sort()
    a.reverse()
    if len(a)>=3:
        return a[2]
    else:
        return max(a)
    
n=int(input())
s=list(map(int,input().split()))
print(po(s,n))