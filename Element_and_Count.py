def po(a):
    c=[]
    for i in a:
        if i not in c:
            c.append(i)
    for i in c:
        print(i,a.count(i),end=" ")

s=int(input())
q=list(map(int,input().split()))
po(q)