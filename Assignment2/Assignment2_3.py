print("Display  factorial")
def main():
    print("enter no:")
    n =int(input())
    f=1
    for i in range(n,1,-1):
        f=f*i
    print("factorial is",f)


if __name__ == "__main__":
    main()