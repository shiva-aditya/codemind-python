i=int(input())
v=[]
c=0
while i:
    p=i%10
    i=i//10
    v.append(p)
for i in range(0,len(v)):
    c=c+((8**i)*v[i])
q=bin(c)
print(q[2::])