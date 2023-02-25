# import big_o

# def heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     l = 2 * i + 1     # left = 2*i + 1
#     r = 2 * i + 2     # right = 2*i + 2
 
#     # See if left child of root exists and is
#     # greater than root
#     if l < n and arr[largest] < arr[l]:
#         largest = l
 
#     # See if right child of root exists and is
#     # greater than root
#     if r < n and arr[largest] < arr[r]:
#         largest = r
 
#     # Change root, if needed
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
#         # Heapify the root.
#         heapify(arr, n, largest)

#     return arr
    
# def kLargest(sample_strings):
# 	# code here

# 	arr = [12, 5, 787, 1, 23]
# 	n = 5
# 	k =2
# 	for i in range(n//2, -1, -1):
# 	    arr = heapify(arr,n, i)
	
# 	# import ipdb; ipdb.set_trace()
# 	for i in range(n-1, 0, -1):
# 	    arr[i], arr[0] = arr[0], arr[i]
# 	    arr = heapify(arr,i,0)
# 	print (*arr)
# 	new_arr = []
# 	# import ipdb; ipdb.set_trace()
# 	for i in range(k):
# 	    new_arr.append(arr[n-i-1])

# 	print(*new_arr)	
# 	# return new_arr

# # arr = [12, 5, 787, 1, 23]
# # lf = kLargest()
# sample_strings = lambda n: 'xx'
# best, others = big_o.big_o(kLargest, sample_strings, n_repeats=100)
# print(best)

    
def find_max_element(arr, low, high):
    mid = low + int((high-low)/2)
    if low <=high:
        if ((mid == 0) or (arr[mid-1]<arr[mid]>arr[mid+1])):
            return arr[mid]
        elif (arr[mid-1]<arr[mid]<arr[mid+1]):
            return find_max_element(arr,(mid+1),high)
        elif (arr[mid-1]>arr[mid]>arr[mid+1]):
            return find_max_element(arr,low,(mid-1))

def findMaximum(arr, n):
    return find_max_element(arr,0,n-1)

arr = [1, 3, 5, 8, 9, 7]
n = 6

print(findMaximum(arr,n))



