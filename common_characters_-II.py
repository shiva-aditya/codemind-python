def po(n,m):
   w=list(n&m)
   w.sort() 
   print(len(w))
        
        

e=input()#"this is python"
e=e.lower()
a=set(e)
a.discard(" ")
r=input()#"this is c"
r=r.lower()
b=set(r)
b.discard(" ")
po(a,b)