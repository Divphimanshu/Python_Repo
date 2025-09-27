#####---- Tuples ----####

a=(1,2,"hello",5.6,True)
print(a)
print(type(a))

# accessing element
print(a[0])  # by index


## Tuple methods
t = (1, 2, 2, 3)
print(t.count(2))   # 2 (occurrences of 2)
print(t.index(3))   # 3 (position of first occurrence of 3)

## built in function
t = (5, 2, 9, 1)
print(len(t))      # 4
print(max(t))      # 9
print(min(t))      # 1
print(sum(t))      # 17
print(sorted(t)) # [1, 2, 5, 9] #convert to list


## Tuple operations
# concat
f = (1, 2)
g = (3, 4)
print(f + g)   # (1, 2, 3, 4)

# repetation
e = (1, 2)
print(e * 3)  # (1, 2, 1, 2, 1, 2)


## Slicing
n = (10, 20, 30, 40, 50, 60)

print(n[1:4])     # (20, 30, 40) → from index 1 to 3
print(n[:3])      # (10, 20, 30) → from start to index 2
print(n[2:])      # (30, 40, 50, 60) → from index 2 to end
print(n[:])       # (10, 20, 30, 40, 50, 60) → full copy
print(n[::2])     # (10, 30, 50) → every 2nd element
print(n[::-1])    # (60, 50, 40, 30, 20, 10) → reversed tuple


## Nested tuple 
k = (1, (2, 3), (4, (5, 6)))

print(k[0])      # 1
print(k[1])      # (2, 3)
print(k[1][0])   # 2
print(k[2][1])   # (5, 6)
print(k[2][0])   # (4)
print(k[2][1][1])# 6
print(k[2][1][0])# 5







