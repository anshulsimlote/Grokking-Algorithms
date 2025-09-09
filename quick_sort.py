# Original data
data = [2, 4, 1, 6, 9, 7, 5, 8]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]   
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]  # handles duplicates properly
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

sorted_data = quick_sort(data)

print(f"Original data: {data}") 
print(f"Sorted data: {sorted_data}")
