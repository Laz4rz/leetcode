arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
#arr = [64, 34, 25, 12, 22, 11, 90, 110]

recursion_depth = 0

def quicksort(arr, start, end):
   """
   just by last element
   """
   if start >= end:
       return arr
   pivot = arr[end]
   n = end
   i = start - 1
   swap = 0

   global recursion_depth
   recursion_depth += 1
   print(10*"=", f" Quicksort: {recursion_depth} ", 10*"=")
   print(f"{start=}, {end=}")
   print(arr)
   print("pivot is:", pivot) 

   for j in range(start, end):
       if arr[j] < pivot:
           i += 1
           print(f"{i=}, {j=}, {arr[j]=}, {arr[i]=}")
           swap = arr[j]
           arr[j] = arr[i]
           arr[i] = swap
   arr[end] = arr[i+1]
   arr[i+1] = pivot

   quicksort(arr, start, i)
   quicksort(arr, i+2, end)
   return arr

arr = quicksort(arr, 0, len(arr)-1)

print(f"\nFinal {arr}")
