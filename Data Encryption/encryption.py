import os
import random
import string

def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(ord(char) ^ key)
    return encrypted_message

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def encrypt_file(file_path, key):
    with open(file_path, 'r') as file:
        original_message = file.read()

    encrypted_message = encrypt(original_message, key)

    random_string = generate_random_string(8)
    encrypted_file_path = f"{random_string}.txt"

    with open(encrypted_file_path, 'w') as encrypted_file:
        encrypted_file.write(encrypted_message)

    print(f"Encryption completed. Encrypted file saved as: {encrypted_file_path}")

    
    os.remove(file_path)
    print(f"Original file '{file_path}' deleted.")

def list_txt_files():
    txt_files = [file for file in os.listdir() if file.endswith(".txt")]
    return txt_files

txt_files = list_txt_files()

if not txt_files:
    print("No text files found in the current folder.")
else:
    print("Available text files:")
    for i, file in enumerate(txt_files, 1):
        print(f"{i}. {file}")

    choice = int(input("Choose a file to encrypt (enter the corresponding number): "))
    if 1 <= choice <= len(txt_files):
        chosen_file = txt_files[choice - 1]
        encryption_key = 126

        encrypt_file(chosen_file, encryption_key)
    else:
        print("Invalid choice. Please choose a valid number.")
