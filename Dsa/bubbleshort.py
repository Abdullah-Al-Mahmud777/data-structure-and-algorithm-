myarray =[7,12,8,9,10,11,6,5,]
n=len(myarray)
for i in range(n):
    for j in range(0,n-i-1):
        if myarray[j]>myarray[j+1]:
            myarray[j], myarray[j+1] = myarray[j+1], myarray[j] 

print("shorted array is:",myarray)