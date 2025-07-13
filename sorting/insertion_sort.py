from typing import List
from enum import Enum

# INSERTION SORT (DONE)
# Complexity: O(n^2)

class Order (Enum):
    asc = "asc"
    desc = "desc"

# def insertion_sort(arr, order="asc"):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             def swap():
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
#             if (arr[j] <= arr[i] and order == "asc"):
#                 swap()
#                 continue
#             if (arr[j] >= arr[i] and order == "desc"):
#                 swap()
#                 continue

#     return arr

def insertion_sort(arr:List[int], order: Order = "asc"):
    if len(arr) == 0:
        return []
    is_desc = order == 'desc'
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if is_desc:
                if arr[j] > arr[i]:
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
            else:
                if arr[j] < arr[i]:
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
    return arr

a = [543, 23, 12, 33, 22, 12, 22, 533, 222]
b = [1, 33, 987, 223, 255, 5522, 12, 342, 879, 29]

print(insertion_sort(a))
print(insertion_sort(b, "descs"))
