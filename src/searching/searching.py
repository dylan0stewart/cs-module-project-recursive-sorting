# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end < start: # 
        return -1
    middle_index = (start + end) // 2 #finding mid by basically taking rounded(down) average of the start/end
    if arr[middle_index] == target: #if mid is the target, then we're done
        return middle_index
    else: #otherwise;
        if target < arr[middle_index]: #if the target is smaller than the mid of array
            end = middle_index - 1 #cut array in half basically by makiung the mid into the new end
            return binary_search(arr, target, start, end) #run binary_search on 'new' halved array
        if target > arr[middle_index]: # if target is larger than mid
            start = middle_index + 1 #take the upper half of array instead
            return binary_search(arr, target, start, end) #and run binary search on it to find index


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
