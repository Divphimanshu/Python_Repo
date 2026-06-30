# create and write file
with open("notes.txt", "w") as file:
    file.write("Welcome to Python")


# read file
with open("notes.txt", "r") as file:
    print(file.read())


# append to file
with open("notes.txt", "a") as file:
    file.write("\nPython is easy.")


# count lines
with open("notes.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
print("Total lines:", count)


# copy file 
with open("source.txt", "r") as source:
    data = source.read()

with open("destination.txt", "w") as destination:
    destination.write(data)