def po(n,m):
    w=list(n&m)
    w.sort()
    if len(w)!=0:
        for i in w:
            print(i,end="")
    else:
        print(-1)





e=input()#"this is python"
e=e.lower()
a=set(e)
a.discard(" ")
r=input()#"this is c"
r=r.lower()
b=set(r)
b.discard(" ")
po(a,b)