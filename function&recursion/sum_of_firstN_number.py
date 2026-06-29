def sum_n(n):
    if n == 0:          # Base case
        return 0
    else:               # Recursive case
        return n + sum_n(n - 1)

# Input from user
n = int(input("Enter a number: "))

# Function call
result = sum_n(n)

print("Sum of first", n, "natural numbers is:", result)