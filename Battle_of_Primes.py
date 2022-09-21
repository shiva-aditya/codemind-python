def po(a,b):
    i=1
    while True:
        c=a+b
        if prime(c+i):
            return i
        else:
            i+=1
def prime(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True
a=int(input())
b=int(input())
print(po(a,b))