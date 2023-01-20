
CheckEven=lambda No:No%2==0
Doubles=lambda No:No*2
Sum=lambda A,B:A+B
def filterX(Helper_Function, Data):
    Result = []
    for no in Data:
        if (Helper_Function(no) == True):
            Result.append(no)
    return Result
def mapX(Helper_Function,Data):
    Result=[]
    for No in Data:
        value=Helper_Function(No)
        Result.append(value)

    return Result

def reduceX(Helper_FUnction,Data):
     Ans=0
     for no in Data:
         Ans=Helper_FUnction(Ans,no)

     return Ans


def main():
    print("Enter numbers of elements you want to enter")
    isize=int(input())
    Data_Input=[]
    print("please enter the data:")
    for iCnt in range(0,isize):
        value=int(input())
        Data_Input.append(value)
    print("Data is:",Data_Input)
    Data_Filter = filterX(CheckEven, Data_Input)
    print("Data filter is:", Data_Filter)
    Data_map=mapX(Doubles,Data_Filter)
    print("Data after map is:",Data_map)
    Output=reduceX(Sum,Data_map)
    print("Result after reduce is:",Output)
if __name__=="__main__":
    main()