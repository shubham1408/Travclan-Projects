def heapify(arr, n, i):
    minimal = i 
    l = 2*i+1
    r = 2*i+2
    
    if r < n and arr[minimal] > arr[l]:
        minimal = l
    if l<n and arr[minimal] > arr[r]:
        minimal = r
    
    if minimal != i:
        arr[i], arr[minimal] = arr[minimal], arr[i]
        heapify(arr,n, minimal)
    
    return arr
    
def kLargest(arr, n, k):
	# code here
	
	for i in range(n//2, -1, -1):
	    arr = heapify(arr,n, i)
	
	import ipdb; ipdb.set_trace()
	for i in range(n-1, 0, -1):
	    arr[i], arr[0] = arr[0], arr[i]
	    arr = heapify(arr,i,0)
	print (*arr)
	new_arr = []
	for i in range(k):
	    new_arr.append(arr[i])
	
	return new_arr

arr = [12, 5, 787, 1, 23]
kLargest(arr, 5, 2)
