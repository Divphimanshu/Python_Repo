###---Nested List---###

rex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rex)       # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access
print(rex[0])    # [1, 2, 3]   (first inner list)
print(rex[0][1]) # 2          (2nd element of the 1st inner list)


#creating n-list
a=[1,2,3]
b=[4,5,6]
c=[a,b]
print(c)
