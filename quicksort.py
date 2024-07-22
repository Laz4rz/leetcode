arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
# def median_of_3(arr):
    

def quicksort(arr, start, end):
   """
   choosing pivot by the median-of-the-three method
   not yet
   just by last element
   """
   pivot = arr[end]
   n = end
   i = -1
   swap = 0

   print(10*"=", " Quicksort ", 10*"=")
   print(arr)
   print("pivot is:", pivot)
   
   for j in range(end):
       if arr[j] <= pivot:
           i += 1
           print(f"{i=}, {j=}, {arr[j]=}, {arr[i]=}")
           swap = arr[j]
           arr[j] = arr[i]
           arr[i] = swap
   arr[end] = arr[i+1]
   arr[i+1] = pivot
   
   print(arr)
   return arr

arr2 = quicksort(arr, 0, len(arr)-1)
arr3 = quicksort(arr, 0, 3)
arr4 = quicksort(arr, 0, 1)
