
values = [10,20,60,40,70]

for i in range(0,len(values)):
    for j in range(i+1,len(values)):
        if values[i]>values[j]:
            null=values[i]
            values[i]=values[j]
            values[j]=null
print("assending order is:",values)
for i in range(0,len(values)):
    for j in range(i+1,len(values)):
        if values[i]<values[j]:
            null=values[i]
            values[i]=values[j]
            values[j]=null
print("discending order is:",values)





















