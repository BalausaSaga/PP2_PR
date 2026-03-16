import os
import shutil

# 3. Find files by extension
print("Searching for .txt files:")

source_path = "../file_handling/balausa.txt"

if os.path.exists(source_path):
    # 4. Copy files
    shutil.copy(source_path, "lab_folders/data_storage/balausa_copy.txt")
    print("File 'balausa.txt' copied to lab_folders/data_storage/")
    print("Original file is still in 'file_handling' folder")
else:
    print("File not found in 'file_handling'. Check the path")