def po(n):
    for i in range(n[0],0,-1):
        c=0
        for j in n:
            if j%i==0:
                c+=1
        if c==len(n):
            return i
            
h=int(input())
k=list(map(int,input().split()))
print(po(k))