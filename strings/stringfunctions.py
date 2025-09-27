
name= "himanshu"

### lenght 
print(len(name))

### string.endswith("")
print(name.endswith("shu"))

### string.startswith
print(name.startswith("Him"))
print(name.startswith("him"))

### string count
print(name.count("i"))

### capitalize
print(name.capitalize())


s = "  Python Programming  "

print(s.lower())      # "  python programming  "
print(s.upper())      # "  PYTHON PROGRAMMING  "
print(s.title())      # "  Python Programming  "
print(s.strip())      # "Python Programming"
print(s.replace("Python", "Java"))  # "  Java Programming  "
print(s.split())      # ['Python', 'Programming']
print("-".join(["Python", "is", "fun"]))  # "Python-is-fun"
print(s.find("Prog")) # 9
print(s.count("m"))   # 2



#### Escape sequence####
txt = "Hello\nWorld"   # Newline
print(txt)

txt = "Hello\tWorld"   # Tab
print(txt)

txt = "He said, \"Python is fun!\""
print(txt)
