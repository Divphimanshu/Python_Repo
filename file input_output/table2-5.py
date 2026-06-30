'''Write a program to generate multiplication tables from 2 to 5 and write it to the different files. 
Place these files in a folder for a 13 – year old.'''

import os #Imports the os module to work with folders and files.

# Create a folder named "Tables" if it doesn't already exist
os.makedirs("Tables", exist_ok=True)

# Generate multiplication tables from 2 to 5
for i in range(2, 6):

    # Create a file for each table
    with open(f"Tables/Table_{i}.txt", "w") as file:

        # Write the multiplication table (1 to 10)
        for j in range(1, 11):
            file.write(f"{i} x {j} = {i*j}\n")

print("Multiplication tables from 2 to 5 have been created successfully!")



with open("Tables/Table_2.txt", "r") as file:
    print("\nTable of 2:")
    print(file.read())

with open("Tables/Table_3.txt", "r") as file:
    print("\nTable of 3:")
    print(file.read())

with open("Tables/Table_4.txt", "r") as file:
    print("\nTable of 4:")
    print(file.read())

with open("Tables/Table_5.txt", "r") as file:
    print("\nTable of 5:")
    print(file.read())