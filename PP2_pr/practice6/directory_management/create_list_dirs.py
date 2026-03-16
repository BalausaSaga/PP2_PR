import os

# 1. Create nested directories
os.makedirs("lab_folders/data_storage", exist_ok=True)
print("Nested directories created!")

# 2. List files and folders
print("Current directory list:")
for item in os.listdir("."):
    print(f"- {item}")