def po(n):
    for i in range(0,len(n)):
        if n[i]>n[-1]:
            return False
    return True

for k in range(int(input())):
    d=int(input())
    p=list(map(int,input().split()))
    c=0
    
    for i in range(0,len(p)):
        if p.count(p[0])==d:
            c=0
            break
        if i==0:
            if p[0]>p[1]:
                c+=1
        elif i==len(p)-1:
            if po(p[:d:]):
                c+=1
        elif p[i]>p[i+1]:
            if po(p[:i+1:]):
                c+=1
        
    print("Case #{}: {}".format(k+1,c))
        #1 2 0 7 2 0 2 0---2
        #4 8 15 16 23 42---1
