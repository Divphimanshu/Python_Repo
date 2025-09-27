student = {"name": "Alice", "age": 21, "marks": 90}

print(student.keys())   # dict_keys(['name', 'age', 'marks'])

print(student.values())   # dict_values(['Alice', 21, 90])
 
print(student.items())   # dict_items([('name', 'Alice'), ('age', 21), ('marks', 90)])

student.update({"age": 22, "grade": "A"})
print(student)  
# {'name': 'Alice', 'age': 22, 'marks': 90, 'grade': 'A'}


# fromkeys
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)   # {'a': 0, 'b': 0, 'c': 0}




