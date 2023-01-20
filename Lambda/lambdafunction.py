
#Normal functions / Named functions
def Add (No1,No2):
    return No1+No2

#Lambda function/ Unnamed function
#lambda paramers: body

AddFunction = lambda A,B:A+B

Ans1=Add(10,11)
Ans2=AddFunction(10,11)

print("Addition using normal functtion :",Ans1)
print("Addition using lambda functtion :",Ans2)

print("type of lambd function is :",type(AddFunction))
print("type of lambd function is :",type(Add))