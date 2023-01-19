import os
def Read_file(Filename):
    if(os.path.exists(Filename)):
        fd=open(Filename,"r")
        Data=fd.read()
        print(Data)
        fd.close()

    else:
        print("File is not exist")
        return
def main():
    print("Enter the file name ")
    Name=input()
    Read_file(Name)
if __name__=="__main__":
    main()