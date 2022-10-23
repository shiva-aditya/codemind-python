def po(a):
    ans=0
    i=0
    while a:
        u=a%10
        a=a//10
        ans=ans+(u*(2**i))
        i+=1
    return ans
    
s=int(input())
p=list(map(str,input().split()))
s=""
for i in p:
    s+=str(i)
print(po(int(s)))
    