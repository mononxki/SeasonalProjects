import os

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr(ord(char) ^ key)
    return decrypted_message

def decrypt_and_edit_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'r') as encrypted_file:
        encrypted_message = encrypted_file.read()

    decrypted_message = decrypt(encrypted_message, key)

    
    with open(encrypted_file_path, 'w') as original_file:
        original_file.write(decrypted_message)

    print(f"Decryption completed. The original file '{encrypted_file_path}' is now updated with decrypted contents.")

def list_txt_files_in_folder(folder_path):
    txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]
    return txt_files

current_folder_path = os.getcwd()

txt_files = list_txt_files_in_folder(current_folder_path)

if not txt_files:
    print("No txt files found in the current folder.")
else:
    print("Available txt files:")
    for i, txt_file in enumerate(txt_files, 1):
        print(f"{i}. {txt_file}")

    file_choice = int(input("Enter the number corresponding to the file you want to decrypt: "))

    if 1 <= file_choice <= len(txt_files):
        chosen_file_path = os.path.join(current_folder_path, txt_files[file_choice - 1])
        decryption_key = 126

        decrypt_and_edit_file(chosen_file_path, decryption_key)
    else:
        print("Invalid choice. Please enter a valid number.")
