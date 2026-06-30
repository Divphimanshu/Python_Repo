## READ
f=open("file.txt")
data=f.read()
print(data)
f.close()


## WRITE
st= " hey You are amazing"
f=open("myfile.txt","w")
f.write(st)
f.close()


## with statement
with open("file.txt") as f:
    data=f.read()
    print(data)