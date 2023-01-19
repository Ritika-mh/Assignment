import os
def Write_file(Filename):
    if(os.path.exists(Filename)):
        print("Enter the data that u want to write in the file")
        Data=input()

        fd=open(Filename,"a")
        fd.write(Data)
    else:
        print("File is not exist")
        return
def main():
    print("Enter the file name ")
    Name=input()
    Write_file(Name)
if __name__=="__main__":
    main()