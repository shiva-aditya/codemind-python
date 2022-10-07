def po(a,l):
    ans=[]
    for i in range(0,l,2):
        for j in range(a[i]):
            ans.append(a[i+1])
    return ans 




s=int(input())
a=list(map(int,input().split()))
print(*po(a,s))