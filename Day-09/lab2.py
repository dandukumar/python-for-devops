import os
folders = input("please provide the list of folder names with spaces in between:").split()
for folder in folders:
    files = os.listdir(folder)
    print("listing files for the folder-")
    print(files)