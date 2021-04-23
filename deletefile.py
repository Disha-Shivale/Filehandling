#Delete file
import os
os.remove("newfile.txt")
print("File removed")
print()

#Check file exist or not
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("File not exist")

#Delete folder
print()
os.rmdir("File")
print("Folder deleted")