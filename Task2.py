#2.Write a Python function to reverse a string.

input_string = "DataAnalysis"

# Initialize an empty string to store the reversed string
reversed_string = ''

# Iterate over each character in the input_string from end to start
for char in input_string:
    reversed_string = char + reversed_string

print(reversed_string)  # Output: "sisylanAataD"

#ANS:
#sisylanAataD
