def po(a):
    s=["a","e","i","o","u"]
    for i in a:
        if i in s:
            s.remove(i)
    if len(s)==0:
        return [0]
    else:
        return s





d=input()
print(*po(d))