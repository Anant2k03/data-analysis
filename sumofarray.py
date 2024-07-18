def _findSum(arr, n): 
    if n <= 0: 
        return 0
    else: 
        return _findSum(arr, n - 1) + arr[n - 1] 
arr =[] 
arr = [1, 2, 3, 4, 5,6, 7, 8,9] 
n = len(arr) 
ans =_findSum(arr,n) 
print (ans)