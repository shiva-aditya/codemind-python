def po(a):
    for i in a:
        if i%2!=0:
            return False
    return True




s=int(input())
w=list(map(int,input().split()))
print(po(w))