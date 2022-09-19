def po(h,s,f):
    if h>50 and s>60 and f>100:
        return 10
    elif h>50 and s>60 and f<=100:
        return 9
    elif h<=50 and s>60 and f>100:
        return 8
    elif h>50 and s<=60 and f>100:
        return 7
    elif h>50 or s>60 and f>100:
        return 6
    else:
        return 5

n,m,o=map(int,input().split())
print(po(n,m,o))