#arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
arr = [64, 34, 25, 12, 22, 11, 90, 110]
# def median_of_3(arr):
    

def quicksort(arr, start, end):
   """
   just by last element
   """
   pivot = arr[end]
   n = end
   i = start - 1
   swap = 0

   print(10*"=", " Quicksort ", 10*"=")
   print(f"{start=}, {end=}")
   print(arr)
   print("pivot is:", pivot)
   
   if start >= end:
       return arr

   for j in range(start, end):
       if arr[j] < pivot:
           i += 1
           print(f"{i=}, {j=}, {arr[j]=}, {arr[i]=}")
           swap = arr[j]
           arr[j] = arr[i]
           arr[i] = swap
   arr[end] = arr[i+1]
   arr[i+1] = pivot
   print("front")
   arr = quicksort(arr, start, i)
   print("rear")
   arr = quicksort(arr, i+2, len(arr)-1)
   return arr

arr = quicksort(arr, 0, len(arr)-1)
