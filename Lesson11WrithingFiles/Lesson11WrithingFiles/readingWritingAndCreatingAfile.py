# Create a text file, write content, and read it

# File name
file_name = "example.txt"

# Write content to the file
with open(file_name, 'w') as file:
    file.write("Hello, this is a sample text.")

# Read content from the file
with open(file_name, 'r') as file:
    content = file.read()
    print("Content read from the file:")
    print(content)

