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
    output = (filter(lambda No: No % 2 == 0, Data_Input)map(lambda No: No * 2, Data_Filter)reduce( lambda A, B:A+B, Data_map)))
    print("Result after reduce is:", Output)
if __name__=="__main__":
    main()