import hashlib
from ecdsa import SigningKey, SECP256k1

# Helper function to perform SHA256 followed by RIPEMD160 (hash160)
def hash160(data):
    sha = hashlib.sha256(data).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha)
    return ripemd160.digest()

# Convert private key to compressed public key
def private_key_to_compressed_public_key(private_key_hex):
    private_key_bytes = bytes.fromhex(private_key_hex)
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    public_key = sk.verifying_key
    
    public_key_bytes = public_key.to_string()
    # Compress the public key
    compressed_prefix = b'\x02' if public_key_bytes[32] % 2 == 0 else b'\x03'
    compressed_public_key = compressed_prefix + public_key_bytes[:32]
    
    return compressed_public_key

# Get the hash160 of the compressed public key
def get_hash160_of_public_key(private_key_hex):
    compressed_public_key = private_key_to_compressed_public_key(private_key_hex)
    hashed_public_key = hash160(compressed_public_key)
    return hashed_public_key.hex()  # Return as hex string

# Process input and output files
def process_private_keys(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            private_key_hex = line.strip()  # Remove newline characters
            if len(private_key_hex) == 64:  # Ensure it's a valid 32-byte private key
                hashed_public_key = get_hash160_of_public_key(private_key_hex)
                outfile.write(f"{hashed_public_key}\n")
            else:
                outfile.write("Invalid private key format\n")

# Example usage
input_file = "keys.txt"  # Input file containing private keys
output_file = "hashe160.txt"  # Output file for hashed keys

process_private_keys(input_file, output_file)
print(f"Processed private keys from {input_file} and saved hashed public keys to {output_file}.")
