print("enter no rows")
t=int(input())



for r in range(t):
    print(" ")
    for c in range(r+1):
        print("*",end='')

for r in range(t,0,-1):
    print(" ")
    for c in range(r+1,0,-1):
        print("*",end='')

