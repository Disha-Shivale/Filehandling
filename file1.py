#Print file content with loop
files = open("one.txt", "r")
for i in files:
    print(i)
print()

#Close file
files = open("one.txt", "r")
print(files.read())
files.close()

