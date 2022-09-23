for _ in range(int(input())):
    v=input()
    t=v[::-1]
    c=0
    for i in range(0,len(t)):
        c=c+(int(t[i])*(2**i))
    print(c)
