checkrange= lambda No: 70<=No<=90
Increment= lambda No: No+10

def filterx(Arr,Function_Name):
    Result=[]
    for no in Arr:
        if (Function_Name(no)):
            Result.append(no)
    return Result
def mapx(Arr,Function_Name):
    Result=[]
    for no in Arr:
        value=Function_Name(no)
        Result.append(value)
    return Result

def reducex(Arr):
    Ans=1
    for no in Arr:
        Ans=Ans*no
    return Ans
def main():
    print("Enter numbers of elements you want to enter")
    isize = int(input())
    Data_Input = []
    print("please enter the data:")
    for iCnt in range(0, isize):
        value = int(input())
        Data_Input.append(value)
    print("Data is:", Data_Input)
    Data_filter = list(filterx(Data_Input,checkrange))

    print("Data after filter:",Data_filter)
    Data_map=list(mapx(Data_filter,Increment))
    print("Data  after map:",Data_map)
    Ret=reducex(Data_map)
    print("Data after reduce:",Ret)
if __name__=="__main__":
    main()