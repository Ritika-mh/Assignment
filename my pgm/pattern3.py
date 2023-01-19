print("enter no of  rows")
m= int(input())
n=m+1
k=n//2
for i in range(n,0,-1):
    for j in range(k+n,0,-1):
        print(" ",end=" ")
    k=k+1
    for j in range(2*i-1,0,-1):
        print("*",end=" ")
        
    print()


