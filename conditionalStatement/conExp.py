####---- Conditional Statement and expression ----####


# if
age = 18
if age >= 18:
    print("You are an adult.")


# If-else
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# if-elif-if 
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")


# nested-if
# age = 20
citizen = True
if age >= 18:
    if citizen:
        print("Eligible to vote.")
    else:
        print("Not a citizen.")
else:
    print("Too young to vote.")
    


# logical operator in conditions
age = 22
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")


