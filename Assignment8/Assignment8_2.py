def pattern(No):
    
    if (No>1):

        No=No-1
        pattern(No)
        print(No, "", end='')
def main():
    I=int(input("Enter input:"))
    pattern(I+1)

if __name__=="__main__":
    main()