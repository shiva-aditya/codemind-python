def po(n,q,l):
    ans=[]
    for i in range(0,l):
        s=a[i]+q
        if max(n)<=s:
            ans.append(True)
        else:
            ans.append(False)
    return ans
            





s=int(input())
a=list(map(int,input().split()))
c=int(input())
print(*po(a,c,s))

