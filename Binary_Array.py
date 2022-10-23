def po(a):
    for i in a:
        if i>1:
            return False
    return True







s=int(input())
p=list(map(int,input().split()))
print(po(p))