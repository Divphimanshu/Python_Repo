#recusrion
def fun(n):
    if n == 0:
        return
    print(n)
    fun(n-1)

fun(3)



# factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))



# reverse string
def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("Python"))