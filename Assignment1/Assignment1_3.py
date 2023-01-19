#Demonstration of Addition of two no"
def Addition(value1,value2):
	ans=value1+value2
	return ans
def main():
	no1=int(input("enter no1"))
	no2=int(input("enter no2"))
	sum=Addition(no1,no2)
	print("Addition is:",sum)

if __name__ =="__main__":
	main()