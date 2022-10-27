def po(n,m):
   w=list(n^m)
   w.sort()
   for i in w:
        print(i,end='') 


e=input()
e=e.lower()
a=set(e)
a.discard(" ")
r=input()
r=r.lower()
b=set(r)
b.discard(" ")
po(a,b)
