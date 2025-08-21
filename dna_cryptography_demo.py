'''
    IEEE ICCUBEA 2025 
    Demo for DNA Encoding/Decoding and Encryption/Decryption 

    By: Akash Bopalkar and Hrishikesh Iyer 
'''

# Mapping for binary to DNA
binary_to_dna = {
    "00": "A",
    "01": "T",
    "10": "C",
    "11": "G"
}

# Reverse mapping for DNA to binary
dna_to_binary = {v: k for k, v in binary_to_dna.items()}

# Encryption substitution (DNA base → DNA base)
encrypt_map = {
    "A": "C",
    "T": "G",
    "C": "T",
    "G": "A"
}

# Decryption substitution (reverse of encrypt_map)
decrypt_map = {v: k for k, v in encrypt_map.items()}


# ---------- Encoding ----------
def encode_text_to_dna(text: str) -> tuple[str, str, str]:
    """Convert text into DNA sequence, return raw binary, padded binary, DNA"""
    # Step 1: Convert text to binary
    binary_raw = ''.join(format(ord(ch), '08b') for ch in text)

    # Step 2: Pad binary string to multiple of 32 bits
    padding_len = (32 - (len(binary_raw) % 32)) % 32
    binary_padded = binary_raw.zfill(len(binary_raw) + padding_len)

    # Step 3: Map binary pairs to DNA
    dna_seq = ''.join(binary_to_dna[binary_padded[i:i+2]] for i in range(0, len(binary_padded), 2))

    return binary_raw, binary_padded, dna_seq


# ---------- Decoding ----------
def decode_dna_to_text(dna_seq: str) -> str:
    """Convert DNA sequence back into text"""
    # Step 1: Convert DNA bases to binary
    binary_string = ''.join(dna_to_binary[base] for base in dna_seq)

    # Step 2: Split into 8-bit chunks and convert to ASCII
    chars = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return ''.join(chars).lstrip('\x00')  # remove padding


# ---------- Encryption ----------
def encrypt_dna(dna_seq: str) -> str:
    """Encrypt DNA sequence by substitution mapping"""
    return ''.join(encrypt_map[base] for base in dna_seq)


# ---------- Decryption ----------
def decrypt_dna(encrypted_seq: str) -> str:
    """Decrypt DNA sequence back to original DNA"""
    return ''.join(decrypt_map[base] for base in encrypted_seq)


# ---------- Main Program ----------
if __name__ == "__main__":
    text = input("Enter text to encode: ")
    print("\n--- DNA Cryptography Demo ---")

    # Encode
    binary_raw, binary_padded, dna_seq = encode_text_to_dna(text)
    print("Original Text:", text)
    print("Raw Binary (no padding):", binary_raw)
    print("Padded Binary (32-bit aligned):", binary_padded)
    print("DNA Sequence:", dna_seq)

    # Encrypt
    encrypted_seq = encrypt_dna(dna_seq)
    print("Encrypted DNA:", encrypted_seq)

    # Decrypt
    decrypted_seq = decrypt_dna(encrypted_seq)
    print("Decrypted DNA:", decrypted_seq)

    # Decode
    decoded_text = decode_dna_to_text(decrypted_seq)
    print("Decoded Text:", decoded_text)
