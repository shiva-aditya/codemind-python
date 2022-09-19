def po(n):
    k=sorted(n)
    if n==k:
        return 0
    else:
        return max(n)-min(n)
for _ in range(int(input())):
    s=int(input())
    a=list(map(int,input().split()))
    print(po(a))