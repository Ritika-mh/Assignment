print("enter no of  rows")
n= int(input())

k=n//2
for i in range(0, n+1):
    for j in range(0,k+n):
        print(" ",end=" ")
    k=k-1
    for j in range(0,2*i-1):
        print("*",end=" ")
        
    print()

for i in range(n+1, 0, -1):
    for j in range(k + n, 0, -1):
        print(" ", end=" ")
    k = k + 1
    for j in range(2 * i - 1, 0, -1):
        print("*", end=" ")

    print()


