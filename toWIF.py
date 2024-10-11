# Input and output files
input_file = "wifrandom.txt"
output_file = "wifrandom_modified.txt"

# Strings to prepend and append
prepend_str = "KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qb"
append_str = "zzzzzzz"

# Read the original passwords and modify them
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        password = line.strip()  # Remove any surrounding whitespace/newline
        modified_password = f"{prepend_str}{password}{append_str}"
        outfile.write(modified_password + '\n')

print("Modified passwords saved to 'wifrandom_modified.txt'.")
