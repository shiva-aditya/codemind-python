def po(a,b):
    c=a&b
    return len(c)




a,b=map(int,input().split())
s=set(map(int,input().split()))
d=set(map(int,input().split()))
print(po(s,d))