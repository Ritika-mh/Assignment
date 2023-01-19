def main():
	print("enter no of rows")
	n=int(input())
	for i in range(n+1,0,-1):
		print("")
		for j in range(i-1,0,-1):
			print("*",end='')


if __name__=="__main__":
	main()