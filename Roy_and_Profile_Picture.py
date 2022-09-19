c=int(input())
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a<c or b<c:
        print("UPLOAD ANOTHER")
    elif a==b:
        print("ACCEPTED")
    else:
        print("CROP IT")