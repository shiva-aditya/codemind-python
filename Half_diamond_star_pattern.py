a=int(input())
if a<=2:
    print("The pattern is not possible")
else:
    for i in range(1,a):
        print(i*"*")
    for i in range(a,0,-1):
        print(i*"*")