def po(n,l):
    ans=[]
    for i in range(0,l):
        c=0
        for j in range(0,l):
            if a[i]==a[j]:
                continue
            else:
                if a[i]>a[j]:
                    c+=1
        ans.append(c)
    return ans
                    



s=int(input())
a=list(map(int,input().split()))
print(*po(a,s))