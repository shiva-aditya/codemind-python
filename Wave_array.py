def po(a,l):
    for i in range(0,l-2,2):
        if a[i]>a[i+1] and a[i+1]>a[i+2]:
            return "no"
    return "yes"

e=int(input())
r=list(map(int,input().split()))
print(po(r,e))