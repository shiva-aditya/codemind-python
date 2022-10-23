a,b,c=map(int,input().split())
e=2*a*b*c*512
d=e//1024
print("{}{}".format(d,"KB"))