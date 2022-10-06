def po(n,f,l):
    if f not in n:
        return -1
    else:
        return n.index(f)






o=int(input())
a=list(map(int,input().split()))
d=int(input())
print(po(a,d,o))