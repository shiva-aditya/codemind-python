def po(a,l):
    for i in range(0,l-1):
        if a[i]<a[i+1]:
            return "no"
    return "yes"

e=int(input())
r=list(map(int,input().split()))
print(po(r,e))