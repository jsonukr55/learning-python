def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
  

  
# utility function to print an array */ 
def printArray(arr, size): 
    for i in range(size): 
        print ("% d"% arr[i], end =" ") 
  
   
# Driver program to test above functions */ 
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 
  

