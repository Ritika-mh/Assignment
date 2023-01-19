print("Display  n*n star matrix")
def main():
    print("enter no:")
    n =int(input())
    for i in range(n):
        print("")
        for j in range(n):
            print("*",end="")


if __name__ == "__main__":
    main()