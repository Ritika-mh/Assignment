from sys import *
from os import *
def Script_Tsk(No):
    if No%2==0:
        print("It is even no:")
    else:
        print("It is odd no:")
def  main():
    print("___Python Programming____")
    print("Automation script started with name:",argv[0])

    if (len(argv) !=2):
        print("Error: Insufficient argument")
        print("Use -h for help and use -u for usage of script")
        exit()
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("Help: This script is used to perform__________")
        exit()
    elif(argv[1]=="-U") or (argv[1]=="-u"):
        print("Usage:provide__number of arguments as")
        print("First Argument as:_____")
        print("Secons Argument as:_____")
        exit()
    else:
        Script_Tsk(int(argv[1]))

if __name__=="__main__":
    main()