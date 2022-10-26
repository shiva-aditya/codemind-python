def po(a):
    if len(a)<=2:
        return "no"
    for i in range(2,len(a)):
        if a[i]!=a[i-1]+a[i-2]:
            return "no"
    return "yes"
    

h=int(input())
r=list(map(int, input(). split()))
print(po(r))