#### Set methods ####

s = {1,5,32,5,5,"raj"}
print(s,type(s))


# Add 
s.add(4)  # for single
s.update([6,7]) # for multiple 
print(s)


# remove
s.remove(6) # remove 6, raise key error if not found
s.discard(100)  # remove if found, doesnt show any error if not found
print(s)


# pop()
s.pop()
print(s)     ## removes and return random elements
s.pop()
print(s)
s.pop()
print(s)

# Clear
d={1,3,4,7,3,9}
d.clear()







 
