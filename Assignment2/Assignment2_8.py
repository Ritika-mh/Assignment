def main():
	print("enter no of rows")
	n=int(input())
	for i in range(1,n+1):
		print("")
		for j in range(1,i+1):
			print(j,"",end='')


if __name__=="__main__":
	main()