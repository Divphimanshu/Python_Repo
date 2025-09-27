##### ---List---- ####

names=["himanshu",78,78.9,"roman",True]
print(names[2])


## chnage element
names[0]="grapes"
print(names)


## add element
names.append("mango")  # At end
print(names)

names.insert(3,"tarzan") # at specific index number
print(names)

names.extend(["ewwt","tweet"])
print(names)


## remove an elemnet
names.remove("mango") #specific element
print(names)

names.pop(2) # at index 2
print(names)

last_item = names.pop()
print(names)

rex=["gsfj","lkgsfdu",6,7.8,"67"] # Empty the list
rex.clear()
print(rex)


## Slicing (same as strings)
print(names[0:5:2])


## Sorting
w=[1,4,6,78,34,66,12]
w.sort()
print(w)


## Reverse
w.reverse()
print(w)



