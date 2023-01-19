fd=open("Marvellous.txt",'r')
print("Information about file:",fd)
print("content of whole file")
print(fd.readline())
print("Reading single line from file")
print(fd.readline())

print("Current file position is",fd.tell())
fd.seek(0)

print("Content of whole file")
print(fd.read())

fd.close()

fd=open("Marvellous.txt","a")

fd.write("Python:Automation and Machine Learing\n")
fd.write("Angular :web Development\n")
fd.seek(0)
print(fd.read())
fd.close()