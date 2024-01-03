import os
import shutil
from colorama import init, Fore, Style

def delete_folders(path, folders):
    init()  # Initialize Colorama
    success_count = 0
    error_count = 0

    for folder in folders:
        folder_path = os.path.join(path, folder)

        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            try:
                shutil.rmtree(folder_path)
                print(f"{Fore.GREEN}[SUCCESS] {folder_path} deleted.{Style.RESET_ALL}")
                success_count += 1
            except Exception as e:
                print(f"{Fore.RED}[ERROR] Failed to delete {folder_path}: {str(e)}{Style.RESET_ALL}")
                error_count += 1
        else:
            print(f"{Fore.YELLOW}[WARNING] {folder_path} does not exist.{Style.RESET_ALL}")

    print("\nDeletion summary:")
    print(f"{Fore.GREEN}Success: {success_count}{Style.RESET_ALL}")
    print(f"{Fore.RED}Errors: {error_count}{Style.RESET_ALL}")

# Example usage
path = r"C:\Users\Szymon\AppData\Local\Riot Games"
folders_to_delete = ["League of Legends PBE", "Riot Client"]

delete_folders(path, folders_to_delete)
