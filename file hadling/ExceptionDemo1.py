def main():
    try:
        print("Enter first no")
        no1=int(input())

        print("Enter second no")
        no2 = int(input())


        Ans=no1/no2
        print("Division of two no is:",Ans)

    except ZeroDivisionError:
        print(" Inside ZeroDivisionError")

    except ValueError:
        print("Inside value error")

    except Exception:
        print("Inside Except block")

    finally:
        print("Inside finally block")
if __name__=="__main__":
    main()