import  os
def creatfile(Filename):
    if(os.path.exists(Filename)):
        print("File is already existing")
        return
    else:
        fd = open(Filename, "w")
def main():
    print("Enter the file name to creat")
    Name=input()
    creatfile(Name)
if __name__=="__main__":
    main()