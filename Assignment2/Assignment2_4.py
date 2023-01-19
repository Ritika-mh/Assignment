
def main():
	print("enter no")
	No=int(input())
	Add=0
	for i in range(1, No, 1):
		if No % i == 0:
			Add=Add+i
			#print(i)
	print("Addition of factor is",Add)



if __name__ =="__main__":
	main()