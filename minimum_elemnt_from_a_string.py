def po(a):
    ans=[]
    for i in a:
        if 122>=ord(i)>=97 or 90>=ord(i)>=65:
            ans.append(ord(i))
    u=chr(min(ans))
    r=u.lower()
    if r==u:
        return u
    if r!=u and r in a:
        return r
    else:
        return u
    
    
e=input()
e=e.split()
print(po(e[-1]))