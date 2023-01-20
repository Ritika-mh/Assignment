def checkeven(No):
    return No%2==0
def Increment(No):
    return No+2
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
    Sum=0
    for no in Arr:
        Sum=Sum+no
    return Sum
def main():
    Data=[2,3,1,6,4,5]
    print("original data is:",Data)
    Data_filter = list(filterx(Data,checkeven))

    print("Data after filter:",Data_filter)
    Data_map=list(mapx(Data_filter,Increment))
    print("Data  after map:",Data_map)
    Ret=reducex(Data_map)
    print("Data after reduce:",Ret)
if __name__=="__main__":
    main()