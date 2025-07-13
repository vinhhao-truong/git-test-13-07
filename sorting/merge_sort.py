# MERGE SORT (UNDONE)
# Complexity: O(n x log(n))
def merge_asc(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1

    # Add any remaining elements from the right half
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1
    
    return sorted_arr

def merge_desc(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1
    return sorted_arr
    
        
def merge_sort(arr, order="asc"):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left_half = merge_sort(left, order)
    right_half = merge_sort(right, order)
    
    if order == "desc":
        return merge_desc(left_half, right_half)
    else:
        return merge_asc(left_half, right_half)


a = [543, 23, 12, 33, 22, 12, 22, 533, 222]
b = [1, 33, 987, 223, 255, 5522, 12, 342, 879, 29]

print(merge_sort(a))
print(merge_sort(b))
print(merge_sort(b, "desc"))
