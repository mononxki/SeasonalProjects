import random
import string
import time
import psutil
from colorama import Fore, init, Style

init(autoreset=True)  


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def generate_code():
    return "https://discord.gg/gift/" + generate_random_string(24)


def is_valid_code(code):
    return code.startswith("https://discord.gg/gift/") and len(code) == 31


def check_ram_usage():
    process = psutil.Process()
    ram_usage = process.memory_info().rss / (1024 * 1024)  
    return ram_usage


def main():
    print("Generating and checking Discord Nitro-like codes with RAM usage control...\n")

    while True:
        code = generate_code()
        is_valid = is_valid_code(code)
        ram_usage = check_ram_usage()

        if is_valid:
            status = f"{Style.BRIGHT}{Fore.MAGENTA}Valid"
        else:
            status = f"{Style.BRIGHT}{Fore.MAGENTA}Invalid"

        print(f"{Fore.CYAN}Generated: {code[24:]} {Fore.LIGHTYELLOW_EX}Status: {status} {Fore.LIGHTYELLOW_EX}RAM Usage: {ram_usage:.2f} MB")

        if is_valid:
            print("Valid code format found. Stopping.")
            break
        time.sleep(0)  


if __name__ == "__main__":
    main()
