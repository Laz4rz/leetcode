import random 

random.seed(42)

def random_array(length, bottom, top):
    return [random.randint(bottom, top) for i in range(length)]

arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
#arr = [64, 34, 25, 12, 22, 11, 90, 110]

recursion_depth = 0
n_operations = 0

def quicksort(arr, start, end):
   """
   just by last element
   """
   original = arr[:] # for shallow copy
   if start >= end:
      # assert on sorting invariant:
      # all elements have to match before and after, only position changes
      assert set(original) == set(arr), "dang we lost someone"
      return arr
   pivot = arr[end]
   n = end
   i = start - 1
   swap = 0

   global n_operations
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
       n_operations += 1
   arr[end] = arr[i+1]
   arr[i+1] = pivot

   quicksort(arr, start, i)
   quicksort(arr, i+2, end)
   return arr

arr = quicksort(arr, 0, len(arr)-1)

print(f"\nFinal {arr}")
print(f"Total number of operations: {n_operations}")

# testing suite
recursion_depth = 0
n_operations = 0 
for i in range(100):
    quicksort(random_array(100, 0, 100), 0, 99)
print(f"Average number of operations: {n_operations/100}")
