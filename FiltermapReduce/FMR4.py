from functools import reduce




def main():
    print("Enter numbers of elements you want to enter")
    isize=int(input())
    Data_Input=[]
    print("please enter the data:")
    for iCnt in range(0,isize):
        value=int(input())
        Data_Input.append(value)
    print("Data is:",Data_Input)
    Data_Filter = list(filter(lambda No:No%2==0, Data_Input))
    print("Data filter is:", Data_Filter)
    Data_map=list(map(lambda No:No*2,Data_Filter))
    print("Data after map is:",Data_map)
    Output=reduce(lambda A,B:A+B,Data_map)
    print("Result after reduce is:",Output)
    
if __name__=="__main__":
    main()