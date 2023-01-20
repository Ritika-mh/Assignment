def checkeven(no):
    if (no%2==0):
        return True
    else:
        return False

def checkevenx(no):
    return (no%2==0)
Ret= checkevenx(12)

if(Ret==True):
    print("Its even")
else:
    print("Its odd")