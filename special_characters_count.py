w=input()
c=0
for i in w:
    if 65 <= ord(i) <=90:
        pass
    elif 97 <= ord(i) <=122:
        pass
    elif ord(i)==32:
        pass
    else:
        c+=1
print(c)