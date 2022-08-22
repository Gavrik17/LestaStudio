def quicksort(arr):
   if len(arr) <= 1:
       return arr
   else:
       main = arr[0]
       left = []
       right = []
       last = []
       
       for n in arr:
           if n < main:
               left.append(n)
           elif n > main:
               right.append(n)
           else:
               last.append(n)
            
       return quicksort(left) + last + quicksort(right)


a = [3, 1, 2, 4, 2, 4, 6, 7, 9, 76, 8]
print(quicksort(a))