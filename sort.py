arr = [5,-2,7,1.4,0,9,8,6,1,12] 
n = 1 
while n < len(arr):
     for i in range(len(arr)-n):
          if arr[i] > arr[i+1]:
               arr[i],arr[i+1] = arr[i+1],arr[i]
     n += 1
print(arr)
print("Hello!")