# file_processing.py
from encry_decry import encrypt, decrypt

def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        plaintext = file.read()
        encrypted_text = encrypt(plaintext, shift)

    with open(output_file, 'w') as file:
        file.write(encrypted_text)

def decrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()
        decrypted_text = decrypt(encrypted_text, shift)

    with open(output_file, 'w') as file:
        file.write(decrypted_text)

# Example usage
if __name__ == "__main__":
    input_file = "input.txt"
    encrypted_file = "encrypted.txt"
    decrypted_file = "decrypted.txt"
    shift_value = 3

    # Encrypting
    encrypt_file(input_file, encrypted_file, shift_value)

    # Decrypting
    decrypt_file(encrypted_file, decrypted_file, shift_value)
