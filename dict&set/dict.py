####-- Dictionary --####

# creating dictionary
#empty
my_dict={}
my_dict2=dict()
print(my_dict,my_dict2)
print(type(my_dict2))

# with values
names={"name": "John", "age": 20, "marks": 85}
print(names)

# using dict()
mames=dict(name="John", age=20, marks=85 )
print(mames)


## Access dictionary
print(names["name"])  # using key
print(names.get("name")) # using get()

## Adding and Updating
names["age"]=23  # update
names["subject"]="maths" # add
print(names)

## Removing items
names.pop("subject") 
print(names)


## Nested dictionary
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}
print(students, students["student1"]["name"]) 
