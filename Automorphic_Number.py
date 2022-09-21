def po(a):
    r=a*a
    li=list(str(a))
    sq=list(str(r))
    li.reverse()
    sq.reverse()
    for t in range(0,len(li)):
        if li[t]!=sq[t]:
            return "Not an Automorphic Number"
    return "Automorphic Number"
           
r=int(input())
print(po(r))
