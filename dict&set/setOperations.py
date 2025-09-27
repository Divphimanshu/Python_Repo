#### Set Operations  ####

# Union() / |
a={1,2}
b={2,3}
print(a.union(b))
print(a|b)

# Intersection() / &
a={2,3,4}
b={1,2,3}
print(a.intersection(b))
print(a & b)

# difference() / -
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))   # {1}
print(a - b)             # {1}

# symmetric_difference()
a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))   # {1, 4}
print(a ^ b)                       # {1, 4}

# issubset()
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))   # True

# issuperset()
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))   # True

# isdisjoint()
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))   # True
