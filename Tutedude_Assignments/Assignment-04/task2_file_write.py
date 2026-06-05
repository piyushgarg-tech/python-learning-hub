text_to_write = input("Enter text to write: ")

with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")

text_to_append = input("Enter additional text: ")

with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")

print("\nFinal content:")

with open("output.txt", "r") as file:
    print(file.read())
