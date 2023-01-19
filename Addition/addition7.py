print("Application to Demonstrate Industrial programming")

def Addition(Value1,Value2):
	Ans=Value1+Value2
	return Ans


def main():
	print("Enter First number:")
	no1=int(input())
	
	print("Enter Second number:")
	no2=int(input())
	Sum = Addition(no1,no2)
		
	print("Addition is:",Sum)

if __name__=="__main__":
	main()
