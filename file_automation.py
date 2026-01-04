from pathlib import Path

# Set the current folder
folder = Path(".")

# List all files in the folder
print("Files before renaming:")
for item in folder.iterdir():
    if item.is_file():
        print(item.name)

# Rename the files by adding a prefix
for item in folder.iterdir():
    if item.is_file():
        new_name = f"new_{item.name}"
        item.rename(new_name)

# List all files after renaming
print("\nFiles after renaming:")
for item in folder.iterdir():
    if item.is_file():
        print(item.name)
