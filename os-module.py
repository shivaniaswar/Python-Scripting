import os

# List all files and directories in the current directory
files_and_dirs = os.listdir('.')
print(files_and_dirs)
print("-" * 40)

os.mkdir('example_dir')
os.rmdir('example_dir')

# Create a file and then remove it
with open('example_file.txt', 'w') as f:
    f.write('This is an example file.')

# Remove the file
os.remove('example_file.txt')

cwd = os.getcwd()
print(f"Current Directory: {cwd}")
print("-" * 40)

# Directory you want to traverse
directory = "C:/Users/Ajinkya/Desktop/Demo/Python/Scripting"

# Walk through the directory
for dirpath, dirnames, filenames in os.walk(directory):
    print(f"Current Path: {dirpath}")
    print(f"Directories: {dirnames}")
    print(f"Files: {filenames}")
    print("-" * 40)

