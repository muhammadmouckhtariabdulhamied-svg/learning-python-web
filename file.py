# Define the file path
file_path = "example.txt"
# Open the file in read mode
with open(file_path, "r") as file:
  # Read the contents of the file
  contents = file.read()
  # Print the contents of the file
  print(contents)
