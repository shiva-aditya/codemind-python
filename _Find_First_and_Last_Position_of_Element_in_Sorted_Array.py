def po(n,f,l):
    if f not in n:
        return [-1,-1]
    else:
        ans=[]
        for i in range(0,l):
            if n[i]==f:
                ans.append(i)
                break
        for i in range(l-1,-1,-1):
            if n[i]==f:
                ans.append(i)
                break
        return ans
    
    
s=int(input())
a=list(map(int,input().split()))
q=int(input())
print(*po(a,q,s))