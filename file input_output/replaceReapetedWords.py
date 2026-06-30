'''A file contains a word “Donkey” multiple times. 
You need to write a program which replace this word with ##### by updating the same file.'''

# Open the file in read mode
with open("sample.txt", "r") as file:
    content = file.read()

# Replace the word "Donkey" with "#####"
content = content.replace("Donkey", "#####")

# Open the same file in write mode
with open("sample.txt", "w") as file:
    file.write(content)

print("All occurrences of 'Donkey' have been replaced.")