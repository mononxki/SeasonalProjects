import os
import platform

# Define the command to flush DNS based on the operating system
if platform.system() == "Windows":
    flush_dns_cmd = "ipconfig /flushdns"
else:
    flush_dns_cmd = "sudo killall -HUP mDNSResponder"

# Define the colors for the console output
class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Display a fancy message
print(ConsoleColors.HEADER + "Flushing DNS..." + ConsoleColors.ENDC)

# Execute the command to flush DNS and display the output
os.system(flush_dns_cmd)
print(ConsoleColors.OKGREEN + "DNS cache flushed successfully!" + ConsoleColors.ENDC)
