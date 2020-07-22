# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB) #combine lengths
    merged_arr = [0] * elements #make merged array 

    merged = [] #instantiate empty list

    while len(arrA) != 0 and len(arrB) != 0: #while neither lengths are 0;
        if arrA[0] < arrB[0]: #if the first value in A is smaller than first in B
            merged.append(arrA[0]) #append the A to merged, and drop from arrA
            arrA.remove(arrA[0])
        else: #else, do the same to B  instead
            merged.append(arrB[0])
            arrB.remove(arrB[0])
    if len(arrA) == 0: #if length of A is 0
        merged += arrB #merged is just arrB basically
    else: #otherwise, we'll take the merged list and add all of arrA to it
        merged += arrA
    return merged


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1: #if the array is one value or less
        return arr #no sorting needed, so return it
    else: #otherwise,
        mid = len(arr) // 2 #find mid
        left = merge_sort(arr[:mid]) #create left by taking eveything left of the midpoint
        right = merge_sort(arr[mid:])#same for right 
        return merge(left, right)#merge them together


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
