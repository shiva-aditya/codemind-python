def po(b):
    g=list(str(b))
    c=g.count("6")
    if c>0:
        for i in range(0,len(g)):
            if g[i]=="6":
                g[i]="9"
                break
        return g
    elif c==0:
        return g
t=int(input())
g=po(t)
for j in g:
    print(j,end="")