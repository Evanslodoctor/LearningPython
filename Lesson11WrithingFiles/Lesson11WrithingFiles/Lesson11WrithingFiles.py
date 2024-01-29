fileName = "Demo.txt"
accessMode = "w"
file = open(fileName, mode=accessMode)
file.write("Hello")
file.close()  # It's good practice to close the file after writing

# Now, if you want to read the content, you should open the file in read mode ('r')
file = open(fileName, mode="r")
print(file.read())
file.close()
