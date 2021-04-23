#Open file for reading
f = open("one.txt", "r")
print(f.read())
print()

#Read specified text
f = open("one.txt", "r")
print(f.read(10))
print()

#Print one line only
f = open("one.txt", "r")
print(f.readline())
print()

#Print first two lines
f = open("one.txt", "r")
print(f.readline())
print(f.readline())
print()