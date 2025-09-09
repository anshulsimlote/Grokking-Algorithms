# Original data
data = [2, 4, 1, 6, 9, 7, 5, 8]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

sorted_data = quick_sort(data)

print(f"Original data: {data}") 
print(f"Sorted data: {quick_sort(data)}")