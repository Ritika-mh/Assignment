#Demonstration for identify no is positive or negative or zero  numbers
def main():
	print("enter no:")
	i=int(input())
	if i==0:
		print("no is zero")

	elif i<0:
		print(" no is negative")

	else i>0:
		print("no is positive")
	

if __name__ =="__main__":
	main()