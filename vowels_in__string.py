def po(a):
    s=["a","e","i","o","u","A","E","I","O","U"]
    ans=[]
    for i in a:
       if i in s:
           if i not in ans:
               ans.append(i)
    if len(ans)==0:
        return [-1]
    else:
        return ans





d=input()
print(*po(d))