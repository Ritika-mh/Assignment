import os
def Delet_file(Filename):
    if(os.path.exists(Filename)):
        os.remove(Filename)

    else:
        print("There is no such file")
        return
def main():
    print("Enter the file name to delet ")
    Name=input()
    Delet_file(Name)
if __name__=="__main__":
    main()