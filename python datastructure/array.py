import array
arr= array.array('i',[1,2,3])
print ("new array: ",end=" ")
for i in range (0, 3):
    print(arr[i],end=" ")
print("\r")


print("----------------------append--------------------")
arr.append(4);
print("appended array: ", end=" ")
for i in range (0, 4):
    print(arr[i], end=" ")
    
