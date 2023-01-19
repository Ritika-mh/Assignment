def fact(No):

    if (No<=0):
        return 1
    else:
        return (No*fact(No-1))
Ret=fact(4)
print("Factorial  is:",Ret)
