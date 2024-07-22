arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
# def median_of_3(arr):
    

def quicksort(arr):
   """
   choosing pivot by the median-of-the-three method
   not yet
   """
   pivot = arr[-1]
   n = len(arr)
   i = -1
   swap = 0
   print(10*"=", " Quicksort ", 10*"=")
   print(arr)
   print("pivot is:", pivot)
   for j in range(n):
       if arr[j] <= pivot:
           i += 1
           print(f"{i=}, {j=}, {arr[j]=}, {arr[i]=}")
           swap = arr[j]
           arr[j] = arr[i]
           arr[i] = swap
   arr[-1] = arr[i+1]
   arr[i+1] = pivot
   print(arr)
   return arr
quicksort(arr)
