import math
def po(n,m):
   c=0
   for i in range(n,m+1):
      if p(i):
         c+=1
   return c

def p(n):
   if n<=1:
      return False
   t=int(math.sqrt(n))
   for i in range(2,t+1):
      if n%i==0:
         return False
   return True


a=int(input())
b=int(input())
print(po(a,b))