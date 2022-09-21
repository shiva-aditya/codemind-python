def po(a):
    for i in range(2,a):
        if (i*i)==a:
            return True
    return False
for _ in range(int(input())):
    d=int(input())
    print(po(d))