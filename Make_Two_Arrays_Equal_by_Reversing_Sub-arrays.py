def po(arr,tar):
  arr.sort()
  tar.sort()
  return arr==tar
    
    
f=int(input())
q=list(map(int,input().split()))
s=int(input())
r=list(map(int,input().split()))
print(po(q,r))