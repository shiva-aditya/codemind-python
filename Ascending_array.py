def po(a,l):
    for i in range(1,l):
        if a[i-1]>=a[i]:
            return "no"
    return "yes"

e=int(input())
r=list(map(int,input().split()))
print(po(r,e))