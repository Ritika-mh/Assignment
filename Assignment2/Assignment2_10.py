def main():
	print("how many no u want to count")
	n=int(input())
	m=0
	Add=0
	print("enter  numbers", end="")
	for i in range(n):

		m=input()

		Add=int(Add)+int(m)
		print(end="")

	print("Addition is",Add)

	

if __name__=="__main__":
	main()