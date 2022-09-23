k=input()
a=0
b=0
g=k.split()
for i in g:
    n=[]
    for j in i:
        n.append(ord(j))
    a=a+min(n)
    b=b+max(n)
print(abs(a-b))
        
        
