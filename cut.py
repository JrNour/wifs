# Define the input and output file names
input_file = "private_keys.txt"  # Replace with your actual input file name
output_file = "keys.txt"  # Replace with the desired output file name

# Open the input file for reading and output file for writing
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Process each line in the input file
    for line in infile:
        # Remove the last two characters and write the modified line to the output file
        outfile.write(line[:-3] + '\n')

print(f"Processed file saved as {output_file}")
