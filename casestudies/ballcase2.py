from sklearn import tree
def MarvellousML(weight,surface):
    Featurs = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0],
               [43, 1], [110, 0], [35, 1], [95, 0]]
    Lables = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(Featurs, Lables)
    Result=clf.predict([[weight,surface]])
    if Result==1:
        print("Your object looks like Tennies ball")
    elif Result==2:
        print("Your object looks like ckicket ball")
def main():
    print("_____Marvellous Infosystem by Piyush Khairnar_____")
    print("Enter wight of object")
    weight=int(input())
    print("What is surface of object smooth or rough")
    surface=input()
    if surface.lower()=="rough":
        surface=1
    elif surface.lower()=="smooth":
        surface=0
    else:
        print("Error:Wrong input")
        exit()

    MarvellousML(weight,surface)
if __name__=="__main__":
    main()

