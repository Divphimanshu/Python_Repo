p1="make a lot of money"
p2="buy me"
p3="subscribe me"
p4="hurry up"

message=input(" enter your comment : ")

if((p1 in message)or(p2 in message)or (p3 in message)or (p4 in message)):
    print(" this message is a scam")
else:
    print("have a nice day")    