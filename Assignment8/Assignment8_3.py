def pattern(No):
    
    if (No>0):
        print(No, "", end='')
        No=No-1
        pattern(No)

def main():
    I=int(input("Enter input:"))
    pattern(I)

if __name__=="__main__":
    main()