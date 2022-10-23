def po(a,l):
    for i in range(l):
        if a[i]%2!=0:
            if i%2!=0:
                pass
            else:
                return False
    return True






s=int(input())
w=list(map(int,input().split()))
print(po(w,s))