print("Application to Demonstrate Arithmatic operation")

import addmodule
import submodule
import mulmodule
import divmodule


def main():
    print("value of __name__ from main is", __name__)
    print("Enter First number:")
    no1 = int(input())
    print("Enter Second number:")
    no2 = int(input())

    Sum = addmodule.Addition(no1, no2)
    print("Addition is:", Sum)

    sub = submodule.Substraction(no1, no2)
    print("Substraction is:", sub)

    mul = mulmodule.multiplication(no1, no2)
    print("multiplication is:", mul)

    div = divmodule.division(no1, no2)
    print("division is:", div)


if __name__ == "__main__":
    main()
