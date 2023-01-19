def prime(Data):

        p=0
        for i in range(2, Data):
            if (Data % i) == 0:
                break
            else:
                p = Data
        return p
def double(No):
    return No*2


    for i in range(0, len(values) - 1):
        n1 = values[i]
        n2 = values[i + 1]
        if n1 > n2:
            n1 = n1
        else:
            n1 = n2
    print("greater no is:", n1)


def filterx(Data,Function):
    result=[]
    for no in Data:
        if Function(no):
            result.append(no)
    return result
def mapx(Data,function):
    result=[]
    for no in Data:
        value=function(no)
        result.append(value)
    return result
def reducex(Data):
    for i in range(0, len(Data) - 1):
        n1 = Data[i]
        n2 = Data[i + 1]
        if n1 > n2:
            n1 = n1
        else:
            n1 = n2
    return n1
def main():
    Data_Orginal=[]
    A=int(input("enter number of elements in list "))
    for i in range(A):
        value=int(input())
        Data_Orginal.append(value)
    print("orignal data is:",Data_Orginal)
    #primelist=prime(Data_Orginal)
    Data_filter = list(filterx(Data_Orginal, prime))
    print("Data after filter:",Data_filter)
    Data_map = list(mapx(Data_filter, double))
    print("Data after map:", Data_map)
    Data_reduce=reducex(Data_map)
    print("Data after reduce is:",Data_reduce)





if __name__=="__main__":
    main()