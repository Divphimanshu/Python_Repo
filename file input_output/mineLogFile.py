'''Write a program to mine a log file and find out whether it contains ‘python’.'''

# Open the log file in read mode
with open("log.txt", "r") as file:
    # Read the entire content of the file
    content = file.read()

# Check if the word "python" is present (case-insensitive)
if "python" in content.lower():
    print("The word 'python' is present in the log file.")
else:
    print("The word 'python' is NOT present in the log file.")



'''Write a program to find out the line number where python is present from ques 6.'''
# Open the log file in read mode
with open("log.txt", "r") as file:

    # Read the file line by line with line numbers
    for line_number, line in enumerate(file, start=1):

        # Check if "python" is present (case-insensitive)
        if "python" in line.lower():
            print(f"'python' is present on line {line_number}")