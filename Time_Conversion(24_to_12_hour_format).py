r=input()
r=r.split(":")
if r[0]=="00":
    print("{}:{} AM".format(12,r[1]))
elif int(r[0])==12:
    print("{}:{} PM".format(12,r[1]))
elif int(r[0])<12:
    print("{}:{} AM".format(r[0],r[1]))
elif int(r[0])>12:
    print("{:02d}:{} PM".format(abs(int(r[0])-12),r[1]))
    