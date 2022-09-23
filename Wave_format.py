def po(a):
    a.sort()
    s=a[::-1]
    if len(s)%2==0:
        for i in range(0,len(s),2):
            s[i],s[i+1]=s[i+1],s[i]
    else:
        for i in range(0,len(s)-1,2):
            s[i],s[i+1]=s[i+1],s[i]
    return s
    
    

f=int(input())
p=list(map(int,input().split()))
print(*po(p))