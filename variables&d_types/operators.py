##  Arithmetic Operators ##
a = 10
b = 3
print(a + b)  # Addition → 13
print(a - b)  # Subtraction → 7
print(a * b)  # Multiplication → 30
print(a / b)  # Division (float) → 3.333...
print(a // b) # Floor Division → 3
print(a % b)  # Modulus → 1
print(a ** b) # Exponentiation → 1000


## Relational operators ##
x, y = 5, 10
print(x == y)  # Equal → False
print(x != y)  # Not equal → True
print(x > y)   # Greater than → False
print(x < y)   # Less than → True
print(x >= y)  # Greater or equal → False
print(x <= y)  # Less or equal → True

## Assignment Operators ##
n = 5
n += 3  # n = n + 3 → 8
n -= 2  # n = n - 2 → 6
n *= 4  # n = n * 4 → 24
n /= 6  # n = n / 6 → 4.0
n %= 3  # n = n % 3 → 1.0
n **= 2 # n = n ** 2 → 1.0


## Logical Operators ##
p, q = True, False
print(p and q) # AND → False
print(p or q)  # OR → True
print(not p)   # NOT → False


## Membership Operator ##
nums = [1, 2, 3, 4]
print(3 in nums)      # True
print(5 not in nums)  # True
print('a' in 'chatgpt')  # True


## Identity Operators ##
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)      # True (same object in memory)
print(x is z)      # False (same content, but different object)
print(x == z)      # True (values are equal)
print(x is not z)  # True


## Bitwise Operators ##
a = 10  # 1010 in binary
b = 4   # 0100 in binary
print(a & b)   # 0
print(a | b)   # 14
print(a ^ b)   # 14
print(~a)      # -11
print(a << 2)  # 40
print(a >> 2)  # 2





