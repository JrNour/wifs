import base58
import hashlib

# Input and output files
input_file = "wifrandom_modified.txt"
output_file = "private_keys.txt"

def wif_to_private_key(wif):
    # Decode the WIF using Base58
    decoded_wif = base58.b58decode(wif)
    
    # Remove the first byte (version byte) and the last 4 bytes (checksum)
    private_key_with_checksum = decoded_wif[1:-4]
    
    # Convert to hex
    private_key_hex = private_key_with_checksum.hex()
    
    return private_key_hex

# Read the WIFs and convert them to private keys
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        wif = line.strip()  # Read each WIF from the input file
        private_key = wif_to_private_key(wif)  # Convert WIF to private key
        outfile.write(private_key + '\n')  # Write the private key to the output file

print("Private keys saved to 'private_keys.txt'.")
