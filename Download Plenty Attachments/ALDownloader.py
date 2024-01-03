import os
import requests
import time
from colorama import init, Fore, Style
from json.decoder import JSONDecodeError
from urllib.parse import urlparse, quote


init()


os.makedirs("discord_files", exist_ok=True)


json_links = []
if os.path.isfile('links.json'):
    try:
        with open('links.json', 'r') as json_file:
            json_links = json_file.readlines()
    except JSONDecodeError:
        print(f"{Fore.RED}JSON file content is not in the right format. Skipping JSON file.{Style.RESET_ALL}")

# Check for links in TXT file
txt_links = []
if os.path.isfile('links.txt'):
    with open('links.txt', 'r') as txt_file:
        txt_links = txt_file.read().splitlines()


all_links = json_links + txt_links

if all_links:
   
    for link in all_links:
        try:
            clean_link = urlparse(link.strip()).geturl()  # Clean the URL to remove extra parameters
            encoded_link = quote(clean_link, safe=':/?=&')  
            response = requests.head(encoded_link, allow_redirects=True)  # Send a HEAD request to get headers

            if response.status_code == 200:
                content_type = response.headers.get('content-type')

                if content_type:
                    file_extension = content_type.split('/')[1]  # Extract file extension from content-type
                    file_name = os.path.join("discord_files", f"{hash(link)}.{file_extension}")

                    
                    file_response = requests.get(encoded_link, stream=True)
                    with open(file_name, 'wb') as file:
                        for chunk in file_response.iter_content(chunk_size=1024):
                            file.write(chunk)
                    
                    print(f"{Fore.GREEN}Downloaded:{Style.RESET_ALL} {file_name}")
                else:
                    print(f"{Fore.RED}Unable to determine content type for:{Style.RESET_ALL} {link}")
            else:
                print(f"{Fore.RED}Failed to download:{Style.RESET_ALL} {link}")
        except Exception as e:
            print(f"{Fore.RED}Error while downloading:{Style.RESET_ALL} {link} - {str(e)}")

    
    time.sleep(5)
else:
    print("No links found in either JSON or TXT file.")
