print("Application to Demonstrate Industrial programming")

import addmodule

def main():
	print("value of __name__ from main is",__name__)
	print("Enter First number:")
	no1=int(input())
	
	print("Enter Second number:")
	no2=int(input())

	Sum = addmodule.Addition(no1,no2)
	print("Addition is:",Sum)
	


if __name__=="__main__":
	main()
