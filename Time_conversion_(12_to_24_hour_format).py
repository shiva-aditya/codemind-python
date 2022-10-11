r=input()
r=r.split()
r[0]=r[0].split(":")
if r[1]=="AM" and r[0][0]=="12":
    print("{}:{}".format("00",r[0][1]))
elif r[1]=="AM":
    print("{}:{}".format(r[0][0],r[0][1]))
elif r[1]=="PM" and r[0][0]=="12":
    print("{}:{}".format("12",r[0][1]))
elif r[1]=="PM":
    print("{}:{}".format(int(r[0][0])+12,r[0][1]))
