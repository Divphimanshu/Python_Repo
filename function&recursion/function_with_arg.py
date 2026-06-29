def greet(name):
    gr="hello" + name
    print(gr)

a = greet("harry")
b = greet("dean")
c = greet("sam")

###

def wish(name, ending):
    gr="hello," + name + ending
    print(gr)

a = wish("harry,", "thank you")
b = wish("dean,", "thanks")
c = wish("sam,","tq")


## Function with Multiple Parameters
def add(a, b):
    print(a + b)

add(10, 20)