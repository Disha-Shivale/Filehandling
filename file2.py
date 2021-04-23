#WRITE DATA (APPEND DATA)
files = open("one.txt", "a")
files.write("\nThis is new line in text file")
files.close()
print("Data Added")
print()

#Add data & open file again
f = open("one.txt", "a")
f.write("\nThis is new line... in file...")
f.close()
f = open("one.txt", "r")
print(f.read())
print()

#Overwrite file content
files = open("one.txt", "w")
files.write("This will override all content...")
files.close()
files = open("one.txt", "r")
print(files.read())
print()


