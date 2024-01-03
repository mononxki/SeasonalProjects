import re

def remove_comments(script):
  
    # Remove provided comments
    script = re.sub(r'// Author of This Script:.*\n', '', script)
    script = re.sub(r'// -_UnKn0wN_K0g4m3r_-.*\n', '', script)
    script = re.sub(r'// Site - Source:.*\n', '', script)
    script = re.sub(r'// pastebin.com/u/XXXX.*\n', '', script)
    script = re.sub(r'// pastebin.com/XXXX.*\n', '', script)
    script = re.sub(r'// mediafire.com/folder/XXXX*\n', '', script)
    script = re.sub(r'// Notice:.*\n', '', script)
    script = re.sub(r'// The original and updated table can be obtained here - XXXXX*\n', '', script)
    
    
    return script

# Read the Cheat Engine table file
with open(r'C:\Users\path.txt', 'r') as file:
    table_contents = file.read()

# Remove comments from the table contents
cleaned_table = remove_comments(table_contents)

# Save the cleaned table to a new file
with open(r'C:\Users\clean.txt', 'w') as file:
    file.write(cleaned_table)
