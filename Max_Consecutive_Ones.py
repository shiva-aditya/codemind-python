def po(n,l):
    n.append(0)
    maxx=0
    count=0
    for i in range(0,l+1):
        if n[i]==1:
            count+=1
            #print("count incre",count,"element",n[i])
        else:
            if count>maxx:
                maxx=count
            count=0
    return maxx


r=int(input())
l=list(map(int,input().split()))
print(po(l,r))