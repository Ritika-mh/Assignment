import os
def Filesearch(Filename):
    if os.path.exists(Filename):
        print("File is exist")
    else:
        print("File does not exist")
def main():
    print("Enter file name you want to search")
    Name=input()
    Filesearch(Name)

if __name__=="__main__":
    main()