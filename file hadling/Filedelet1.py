import os
def Delet_file(Filename):
    if(os.path.exists(Filename)):
        size=os.path.getsize(Filename)
        if (size==0):
            os.remove(Filename)
        else:
            print("Are you sure to delet the file? Y/N")
            option=input()
        if(option=="Y" or option=="y"):
            os.remove(Filename)
        else:
            print("File deletion process stopped.")

    else:
        print("There is no such file")
        return
def main():
    print("Enter the file name to delet ")
    Name=input()
    Delet_file(Name)
if __name__=="__main__":
    main()