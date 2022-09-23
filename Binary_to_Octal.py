for _ in range(int(input())):
    f=int(input()) #111000
    d=str(f) #"111000"
    h=d[::-1] #"000111"
    c=0
    for i in range(0,len(h)):
        c=c+(int(h[i])*(2**i))
    p=oct(c)
    print(p[2::])
    