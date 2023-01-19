import os
def Filesearch(Filename):
    if os.path.exists(Filename):
        fd=open(Filename,"r")
        Data=fd.read()
        print(Data)
        fd.close()
    else:
        print("File does not exist")
def main():
    print("Enter file name ")
    Name=input()
    Filesearch(Name)

if __name__=="__main__":
    main()