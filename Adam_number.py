def po(a):#12
    s=a*a #144
    ss=str(a)#"12"
    r=ss[::-1]#"21"
    sq=str(int(r)*int(r))#441
    w=str(s)
    if sq==w[::-1]:
        return True
    else:
        return False
    


f=int(input())
print(po(f))
