# program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
with open("poems.txt", "r") as file:
    content = file.read()

if "twinkle" in content.lower():
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is NOT present in the file.")


