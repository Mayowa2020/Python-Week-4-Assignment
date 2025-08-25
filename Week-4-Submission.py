# Read from the input file
with open('input.txt', 'r') as file:
    data = file.read()

print("Before:", data)  # Check the original content

# Modify the content
data = data.replace('God is good!', 'God is great!')

print("After:", data)   # See if anything changed

# Write the modified content to the output file
with open('output.txt', 'w') as file:
    file.write(data)

