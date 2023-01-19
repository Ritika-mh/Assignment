
def main():
	print("enter no")
	No=int(input())
	for i in range(2, No):
		if No % i == 0:
			print(No,"is not prime number")
			break
	else:
			print(No,"is prime number")




if __name__ =="__main__":
	main()