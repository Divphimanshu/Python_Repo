####---- SET ----####


# creation
# empty set (must use set(), {} is a dict)
s = set()
print(s)

# from iterable
s1 = set([1, 2, 2, 3])        # -> {1, 2, 3}
s2 = set("hello")             # -> {'h','e','l','o'}
print(s1,s2)

# set literal
s3 = {1, 2, 3}
print(s3)

# frozenset (immutable)
fs = frozenset([1, 2, 3])
print(fs)


