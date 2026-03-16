import shutil
import os

# 3. Append new line
with open("balausa.txt", "a") as f:
    f.write("Nationality: Kazakh\n")
print("New line")

# 4. Copy and back up using shutil
shutil.copy("balausa.txt", "balausa_backup.txt")
print("Backup created: balausa_backup.txt")

# 5. Delete files safely
if os.path.exists("balausa_backup.txt"):
    os.remove("balausa_backup.txt")
    print("Backup deleted safely.")