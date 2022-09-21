def po(a):
    f=a*a
    s=[]
    while f:
        h=f%10
        f=f//10
        s.append(h)
    if sum(s)==a:
        return "Neon Number"
    else:
        return "Not Neon Number"
f=int(input())
print(po(f))