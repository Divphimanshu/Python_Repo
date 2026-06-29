def remove_and_strip(words, word):
    new_list = []

    for item in words:
        if item.strip() != word:
            new_list.append(item.strip())

    return new_list

# Example list
words = ["  Apple ", " Banana ", " Mango ", " Banana ", " Grapes "]

# Function call
result = remove_and_strip(words, "Banana")

print(result)